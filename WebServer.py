import json
import Food
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging


menu = Food.getMenu()
class S(BaseHTTPRequestHandler):
    def parse_get_request(self, path):
        if path.startswith("/drinks"):
            if path == "/drinks":
                #return all ids
                return Food.print_food_by_type(menu["drink"])
            else:
                id_num = path[len("/drinks")+1:]
                try:
                    print(path)
                    print(id_num)
                    id_num = int(id_num)
                    return Food.print_specific_item(menu["drink"][id_num])
                except:
                    print("Error during convert id")
        elif path.startswith("/pizzaz"):
            if path == "/pizzaz":
                #return all ids
                return Food.print_food_by_type(menu["pizza"])
            else:
                id_num = path[len("/pizzaz")+1:]
                try:
                    print(path)
                    print(id_num)
                    id_num = int(id_num)
                    return Food.print_specific_item(menu["pizza"][id_num])
                except:
                    print("Error during convert id")
        elif path.startswith("/desserts"):
            if path == "/desserts":
                #return all ids
                return Food.print_food_by_type(menu["dessert"])
            else:
                id_num = path[len("/desserts")+1:]
                try:
                    print(path)
                    print(id_num)
                    id_num = int(id_num)
                    return Food.print_specific_item(menu["dessert"][id_num])
                except:
                    print("Error during convert id")
        else:
            return "Invalid Request\r\n"
    def parse_post_request(self, path, data):
        if path != "/order":
            return "Invalid Request\r\n"
        response = "Response - "
        total_price = 0
        try:
            #print(data)
            order_dict = json.loads(data)
            #print(order_dict.keys())
            if "drinks" in order_dict.keys():
                for id in order_dict["drinks"]:
                    total_price += menu["drink"][int(id)].price
            if "desserts" in order_dict.keys():
                for id in order_dict["desserts"]:
                    total_price += menu["dessert"][int(id)].price
            if "pizzaz" in order_dict.keys():
                for id in order_dict["pizzaz"]:
                    total_price += menu["pizza"][int(id)].price
        except:
            print("Invalid dict")

        answer = {}
        answer['price']= total_price
        response += str(answer) + "\r\n"
        return response
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        #logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        resp = self.parse_get_request(self.path)
        self._set_response()
        self.wfile.write(resp.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",str(self.path), str(self.headers), post_data.decode('utf-8'))
        resp = self.parse_post_request(self.path, post_data)
        self._set_response()
        self.wfile.write(resp.encode('utf-8'))
    
#go to localhost:8080 to check the server
def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
