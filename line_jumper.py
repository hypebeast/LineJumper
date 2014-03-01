import sublime, sublime_plugin

class LineJumperCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        settings = sublime.load_settings("LineJumper.sublime-settings")
        number_of_lines = settings.get('number_of_lines')
        cmd_args = {}

        if not ('cmd' in args):
            return

        if 'number_of_lines' in args:
            number_of_lines = args['number_of_lines']

        if args['cmd'] == 'up':
            cmd = 'move'
            cmd_args = {'by': 'lines', 'forward': False}
        elif args['cmd'] == 'down':
            cmd = 'move'
            cmd_args = {'by': 'lines', 'forward': True}
        elif args['cmd'] == 'up_select':
            cmd = 'move'
            cmd_args = {'by': 'lines', 'forward': False, 'extend': True}
        elif args['cmd'] == 'down_select':
            cmd = 'move'
            cmd_args = {'by': 'lines', 'forward': True, 'extend': True}

        for i in range(number_of_lines):
            self.view.run_command(cmd, cmd_args)
