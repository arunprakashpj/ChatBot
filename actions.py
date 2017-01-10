import info

def format_results(response_message,results):
    i = 1
    for result in results:
        response_message += str(i)+") " +result+"\n"
        i += 1
    return response_message
    
#get response_message for products or services
def get_info(entity):
    results = []
    response_message = "This is my default reply...."
    return format_results(response_message,results)
