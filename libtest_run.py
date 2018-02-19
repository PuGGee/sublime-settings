import os
import sublime
import sublime_plugin
import re

from ShellCommand.ShellCommand import ShellCommandCommand

class LibTestCommand(ShellCommandCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            file_name = self.view.file_name()
            
            title = "* TEST *"
            command = "cd " + self.get_project_dir() + " && ~/.rvm/bin/rvm-auto-ruby -S bundle exec ruby -I\"lib:test\" " + file_name + " -n"
            
            ShellCommandCommand.run(self,
                                    edit,
                                    command=command,
                                    region=True,
                                    arg_required=True,
                                    syntax="RSpec",
                                    title=title)
    
    def get_project_dir(self):
        return re.search('(/.*)/test/', self.view.file_name()).group(1)
