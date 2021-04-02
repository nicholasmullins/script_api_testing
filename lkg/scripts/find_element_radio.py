import logging
import json

log = logging.getLogger(__name__)

def run(context):
    element_info = context.find_element('inp_radio')
    json_string = json.dumps(element_info)
    parseable_unicode = json.loads(json_string)
    
    string_and_variable = 'RADIO (SELECTED):\n\n' + ' ' + json_string


    context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', string_and_variable)