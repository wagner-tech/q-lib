import argparse
import q
import sqlite3
sqlite3.enable_callback_tracebacks(True)

class QIF(object):
    '''
    QIF is the interface class to q
    '''


    def __init__(self, option_dict):
        p = q.configparser.ConfigParser()
        qrc_filename = 'None'
        
        # set option defaults
        args_dummy, self.options, parser_dummy = q.initialize_command_line_parser(p, qrc_filename)
        
        for opt in option_dict.keys():
            if opt in ["d", "delimiter"]:
                self.options.delimiter = option_dict[opt]
            elif opt in ["H", "skip-header"]:
                self.options.skip_header = True
            else:
                raise RuntimeError("Unknown option: "+opt)
    
    def request(self, sql):
        
        args = [sql]
        
        #dump_defaults_and_stop__if_needed(options, parser)
    
        #dump_version_and_stop__if_needed(options)
    
        STDOUT_dummy, default_input_params, q_output_printer_dummy, query_strs_dummy = q.parse_options(args, self.options)
    
        data_streams_dict = q.initialize_default_data_streams()
    
        q_engine = q.QTextAsData(default_input_params=default_input_params,data_streams_dict=data_streams_dict)
    
        #q.execute_queries(STDOUT, options, q_engine, q_output_printer, query_strs)
        q_output = q_engine.execute(sql, save_db_to_disk_filename=self.options.save_db_to_disk_filename)
        
        q_engine.done()
        
        if q_output.error:
            return q_output.error
        return q_output.data


if __name__ == '__main__':
    qif = QIF({"d" : ";", "H" : 1})
    data = qif.request("select Vorname,Nachname from /home/sparky2021/SVBaL/tmp/export.csv")
    
    print(data)
    