# ************************************************************************
# Title:                    {{controller_title}}
# Description:              {{controller_description}}
# Author:                   {{author}} <{{author_email}}>
# Original Date:            {{generation_date}}
# Version:                  {{version}}
# ************************************************************************
from . import BaseController

class {{controller_name}}(BaseController):

      def __init__(self):
          pass

      def index(self, request, response):
         return self.Views.render_view("home.html")

