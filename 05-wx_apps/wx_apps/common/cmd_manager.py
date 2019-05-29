# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/29 16:58
from flask_script import Manager as BaseManager, Option, Command, safe_actions, iteritems


class Manager(BaseManager):
    """托管程序"""

    def option(self, *args, **kwargs):
        """向每个函数中加入环境类型"""
        option1 = Option("-m", "--model", help="运行的模式: 1. 生产模式 2. 测试模式", dest="model", default=1)
        option = Option(*args, **kwargs)

        def decorate(func):
            name = func.__name__

            if name not in self._commands:
                command = Command()
                command.run = func
                command.__doc__ = func.__doc__
                command.option_list = []

                self.add_command(name, command)

            self._commands[name].option_list.append(option)
            self._commands[name].option_list.append(option1)
            return func

        return decorate

    def handle(self, prog, args=None):
        self.set_defaults()
        app_parser = self.create_parser(prog)

        args = list(args or [])
        app_namespace, remaining_args = app_parser.parse_known_args(args)

        # get the handle function and remove it from parsed options
        kwargs = app_namespace.__dict__
        func_stack = kwargs.pop('func_stack', None)
        if not func_stack:
            app_parser.error('too few arguments')

        last_func = func_stack[-1]
        if remaining_args and not getattr(last_func, 'capture_all_args', False):
            app_parser.error('too many arguments')

        args = []
        for handle in func_stack:

            # get only safe config options
            config_keys = [action.dest for action in handle.parser._actions
                           if handle is last_func or action.__class__ in safe_actions]

            # pass only safe app config keys
            config = dict((k, v) for k, v in iteritems(kwargs)
                          if k in config_keys)

            # remove application config keys from handle kwargs
            kwargs = dict((k, v) for k, v in iteritems(kwargs)
                          if k not in config_keys)
            print(kwargs)

            if handle is last_func and getattr(last_func, 'capture_all_args', False):
                args.append(remaining_args)
            try:
                res = handle(*args, **config)
            except TypeError as err:
                err.args = ("{0}: {1}".format(handle, str(err)),)
                raise

            args = [res]

        assert not kwargs
        return res
