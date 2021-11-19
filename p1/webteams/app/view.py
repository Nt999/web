# coding: utf-8

import codecs
import os.path

from .templite import Templite

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.lookup_o = TemplateLookup('./templates')

   #-------------------------------------------------------
   def createList_px(self, data_opl):
   #-------------------------------------------------------
        if (listform == 'tabelle'):
            template_o = self.lookup_o.get_template('list.tpl')
            listformNow = "tabelle"
            listformNew = "liste"               #Für die umschalter
            listformNewText = "Liste"
        elif (listform == 'liste'):
            template_o = self.lookup_o.get_template('list2.tpl')
            listformNow = "liste"
            listformNew = "tabelle"
            listformNewText = "Tabelle"

        markup_s = template_o.render(data_o = data_opl, listformNow = listformNow, listformNew = listformNew, listformNewText = listformNewText)
        return markup_s

   #-------------------------------------------------------
   def createForm_px(self, id_spl, data_opl):
   #-------------------------------------------------------
      template_s = self.readFile_p('form.tpl.html')
      template_o = Templite(template_s)
      markup_s = template_o.render(data_o = data_opl, key_s = id_spl)
      return markup_s

   #-------------------------------------------------------
   def readFile_p(self, fileName_spl):
   #-------------------------------------------------------
      content_s = ''
      with codecs.open(os.path.join('templates', fileName_spl), 'r', 'utf-8') as fp_o:
         content_s = fp_o.read()
      return content_s
# EOF