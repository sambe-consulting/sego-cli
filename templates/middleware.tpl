# ************************************************************************#
# Title:                    {{middleware_name}}                           #
# Description:              {{controller_description}}                    #
# Author:                   {{author}} <{{author_email}}>                 #
# Original Date:            {{generation_date}}                           #
# Version:                  {{version}}                                   #
# ************************************************************************

from sego.Middleware.Middleware import Middleware
from sego.Middleware.MiddlewareManager import MiddlewareManager
from webob import Response, Request

class {{middleware_name}}(Middleware):

      def __init__(self):
          pass

      def process_request(self, request: Request):
          print("Processing request", request.url)

      def process_response(self, request: Request, response: Response):
          print("Processing response", request.url)

