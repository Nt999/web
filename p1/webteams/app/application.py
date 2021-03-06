# coding: utf-8
import cherrypy
from .database import Database_cl
from .view import View_cl

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()

   @cherrypy.expose
   #-------------------------------------------------------
   def index(self,listformNow = "tabelle"):
   #-------------------------------------------------------
      return self.createList_p(listformNow)

   @cherrypy.expose
   #-------------------------------------------------------
   def add(self,listformNow):
   #-------------------------------------------------------
      return self.createForm_p(listformNow)

   @cherrypy.expose
   #-------------------------------------------------------
   def edit(self, id_spl,listformNow):
   #-------------------------------------------------------
      return self.createForm_p(id_spl,listformNow)

   @cherrypy.expose
   #-------------------------------------------------------
   def save(self,listformNow, id_spa, name1_spa, vorname1_spa, matrnr1_spa, name2_spa, vorname2_spa, matrnr2_spa,semanzahl1,semanzahl2):
   #-------------------------------------------------------
      id_s = id_spa
      data_a = [ name1_spa, vorname1_spa, matrnr1_spa, name2_spa, vorname2_spa, matrnr2_spa,semanzahl1,semanzahl2 ]
      if id_s != "None":
         self.db_o.update_px(id_s, data_a)
      else:
         self.db_o.create_px(data_a)
      return self.createList_p(listformNow)

   @cherrypy.expose
   #-------------------------------------------------------
   def delete(self, id, listformNow):
   #-------------------------------------------------------
       self.db_o.delete_px(id)
       raise cherrypy.HTTPRedirect('/?listformNow=' + listformNow)

   @cherrypy.expose


   #-------------------------------------------------------
   def default(self, *arguments, **kwargs):
   #-------------------------------------------------------
      msg_s = "unbekannte Anforderung: " + \
      str(arguments) + \
      ' ' + \
      str(kwargs)
      raise cherrypy.HTTPError(404, msg_s)
   default.exposed= True

   #-------------------------------------------------------
   def createList_p(self, listformNow):
   #-------------------------------------------------------
      data_o = self.db_o.read_px()
      return self.view_o.createList_px(data_o, listformNow)

   #-------------------------------------------------------
   def createForm_p(self,listformNow, id_spl = None):
   #-------------------------------------------------------
      if id_spl != None:
         data_o = self.db_o.read_px(id_spl)
      else:
         data_o = self.db_o.getDefault_px()
      return self.view_o.createForm_px(listformNow,id_spl, data_o)
# EOF
