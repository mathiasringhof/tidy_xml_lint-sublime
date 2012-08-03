import sublime, sublime_plugin, subprocess
 
class TidyXmlLintCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    command = "XMLLINT_INDENT=$'\t' xmllint --format --encode utf-8 -"
    # help from http://www.sublimetext.com/forum/viewtopic.php?f=2&p=12451
    xml = self.view.substr(self.view.sel()[0])
    if (xml == ""): xml = self.view.substr(sublime.Region(0, self.view.size()))
    p = subprocess.Popen(command, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    result, err = p.communicate(xml.encode('utf-8'))
 
    if err != "":
      self.view.set_status('xmllint', "xmllint: "+err)
      sublime.set_timeout(self.clear,10000)
    else:
      self.view.replace(edit, self.view.sel()[0], result.decode('utf-8'))
      sublime.set_timeout(self.clear,0)
 
  def clear(self):
    self.view.erase_status('xmllint')