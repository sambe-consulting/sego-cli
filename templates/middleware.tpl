# ************************************************************************#
# Title:                    {{middleware_name}}                           #
# Description:              {{middleware_description}}                    #
# Author:                   {{author}} <{{author_email}}>                 #
# Original Date:            {{generation_date}}                           #
# Version:                  {{version}}                                   #
# ************************************************************************

from sego.Middleware.Middleware import Middleware
from sego.Middleware.MiddlewareManager import MiddlewareManager
from flask import request
class {{middleware_name}}(Middleware):

      def __init__(self):
          pass

      def process_request(self, request):
          print("Processing request", request.url)

      def process_response(self, request, response):
          print("Processing response", request.url)

