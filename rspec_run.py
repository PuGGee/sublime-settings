import os
import sublime
import sublime_plugin
import re

from ShellCommand.ShellCommand import ShellCommandCommand

class RspecCommand(ShellCommandCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            line = self.view.rowcol(self.view.sel()[0].end())[0] + 1
            file_name = self.view.file_name()
            
            title = "* RSPEC *"
            command = "cd " + self.get_project_dir() + " && ~/.rvm/bin/rvm-auto-ruby -S bundle exec rspec " + file_name + ":" + str(line)
            
            ShellCommandCommand.run(self,
                                    edit,
                                    command=command,
                                    syntax="RSpec",
                                    title=title)
    
    def get_project_dir(self):
        return re.search('(/.*)/spec/', self.view.file_name()).group(1)
