#!/usr/bin/env python3 

"""Define of HBnB console  

""" 

import re 

import cmd 

import json 

from models import storage 

from models.base_model import BaseModel 

from models.user import User 

from models.state import State 

from models.city import City 

from models.amenity import Amenity 

from models.place import Place 

from models.review import Review 

  

  

class HBNBCommand(cmd.Cmd): 

  

    """class of cmd  

    """ 

    prompt = "(hbnb) " 

    cl_dict = { 

            "BaseModel": BaseModel, 

            "User": User, 

            "State": State, 

            "City": City, 

            "Amenity": Amenity, 

            "Place": Place, 

            "Review": Review 

            } 

  

    def do_create(self, line): 

        """ class instance 

        """ 

        if not line: 

            print("** class name missing **") 

        else: 

            if line not in HBNBCommand.cl_dict: 

                print("** class doesn't exist **") 

            else: 

                our_model = HBNBCommand.cl_dict[line]() 

                our_model.save() 

                print(our_model.id) 

  

    def do_show(self, line): 

        """For instance, prints string repr 

        """ 

        key = our_obj(line) 

        if key: 

            our_dict = storage.all() 

 

            print(our_dict[key]) 

  

    def do_destroy(self, line): 

        """Removes an instance according to class name and id 

        """ 

  

        key = our_obj(line) 

        if key: 

            fl_dict = storage.all() 

            del fl_dict[key] 

            storage.save() 

  

    def do_all(self, line): 

        """For objects, prints string representation  

""" 

        our_dict = storage.all() 

        our_list = [] 

        if len(line) == 0: 

            for values in our_dict.values(): 

                our_list.append(str(values)) 

            print(our_list) 

        else: 

            if line not in HBNBCommand.cl_dict: 

                print("** class doesn't exist **") 

            else: 

                for value in our_dict.values(): 

                    if value.to_dict()["__class__"] == line: 

                        our_list.append(str(value)) 

                print(our_list) 

  

    def do_update(self, line): 

        """ Instance update  """ 

  

        our_list = parse(line) 

        key = our_obj(line) 

        if key: 

            if len(our_list) > 4: 

                print("Usage:update <class name> <id>\ 

                         <aittribute name> \"<attribute value>\"") 

            elif len(our_list) == 3: 

                print("** value missing **") 

            elif len(our_list) == 2: 

                print("** attribute name missing **") 

            else: 

                our_dict = storage.all() 

                my_in = our_dict[key] 

                val = our_list[3][1:-1] 

                try: 

                    if "." in val: 

                        val = float(val) 

                    else: 

                        val = int(val) 

                except ValueError: 

                    pass 

                setattr(my_in, our_list[2], val) 

                storage.save() 

  

    def do_EOF(self, line): 

        """End of program command 

        """ 

  

        return True 

  

    def do_quit(self, line): 

        """end the program 

        """ 

  

        return True 

  

    def emptyline(self): 

  

        pass 

  

  

def parse(arg): 

  

    """line split 

    """ 

  

    return arg.split() 

  

  

def our_obj(my_line): 

  

    """ object key return 

    """ 

  

    our_list = parse(my_line) 

    if len(our_list) == 0: 

        print("** missing class name **") 

    elif len(our_list) == 1: 

        if our_list[0] not in HBNBCommand.cl_dict: 

            print("** class non existent **") 

        else: 

            print("** instance id missing **") 

    elif len(our_list) >= 2: 

        if our_list[0] not in HBNBCommand.cl_dict: 

            print("** class  non existent **") 

        else: 

            key = f"{our_list[0]}.{our_list[1]}" 

            fl_dict = storage.all() 

            if key in fl_dict: 

                return key 

            else: 

                print("** instance not found **") 

  

  

if __name__ == '__main__': 

    HBNBCommand().cmdloop() 
