import threading
from burp import IBurpExtender, IContextMenuFactory, IContextMenuInvocation
from javax.swing import JMenuItem
from threading import Thread

class BurpExtender(IBurpExtender, IContextMenuFactory):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._context = None
        callbacks.setExtensionName("Multi-Request-Repeater")
        callbacks.registerContextMenuFactory(self)

    def createMenuItems(self, contextMenuInvocation):
        self._context = contextMenuInvocation
        menu_list = []
        menu_list.append(JMenuItem("Repeat Selected Requests", actionPerformed=self.actionPerformed))
        return menu_list

    def actionPerformed(self, event):
        selected_messages = self._context.getSelectedMessages()
        timeout = 30000  # 30 seconds
        for message in selected_messages:
            # Send the message to the server
            http_service = message.getHttpService()
            request = message.getRequest()
            thread = threading.Thread(target=self.send_request, args=(http_service, request, timeout))
            thread.start()

    def send_request(self, http_service, request, timeout):
        response = None
        try:
            response = self._callbacks.makeHttpRequest(http_service, request, timeout)
        except Exception as e:
            print(e)
        return response
