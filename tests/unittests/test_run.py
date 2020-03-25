""" Unit tests for run.py/Command Line Interface """

import pytest
import run

################################## CMD SETUP ################################
app = run.replShell()

################################ TEST COMMANDS ##############################
# Test list and maybe save/load

################################### CLASS ###################################
################################## TEST ADD #################################
def test_do_add(capsys): 
    app.do_add("TestAddEmpty")
    captured = capsys.readouterr()
    assert captured.out == "Successfully added class 'TestAddEmpty'\n"
    app.do_list("")
    captured = capsys.readouterr()
    assert captured.out == "TestAddEmpty\n\n"

def test_do_add_duplicate(capsys):
    app.do_add("TestAddEmpty")
    captured = capsys.readouterr()
    assert captured.out == "Successfully added class 'TestAddEmpty'\n"
    app.do_add("TestAddEmpty")
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Unable to add class 'TestAddEmpty'\n"
    app.do_list("")
    captured = capsys.readouterr()
    assert captured.out == "TestAddEmpty\n\n"

def test_do_add_more(capsys):
    app.do_add("TestAddMore")
    captured = capsys.readouterr()
    assert captured.out == "Successfully added class 'TestAddMore'\n"
    app.do_add("TestAdd1More")
    captured = capsys.readouterr()
    assert captured.out == "Successfully added class 'TestAdd1More'\n"
    app.do_list("")
    captured = capsys.readouterr()
    assert captured.out == "TestAddMore\nTestAdd1More\n\n"

def test_do_add_none(capsys):
    app.do_add("")
    captured = capsys.readouterr()
    assert captured.out == "Usage: add <class_name1>, <class_name2>, ... , <class_nameN>\n"
    
    #TODO 
    # test the list with no classes added (shouldn't output a giant error msg like it does now)

def test_do_add_multi(capsys):
    app.do_add("Multi1, Multi2, Multi3")
    captured = capsys.readouterr()
    assert captured.out == "Successfully added class 'Multi1'\nSuccessfully added class 'Multi2'\nSuccessfully added class 'Multi3'\n"

    app.do_list("")
    captured = capsys.readouterr()
    assert captured.out == "Multi1\nMulti2\nMulti3\n\n"

################################ TEST DELETE ################################
def test_do_delete(capsys):
    #Need to capture the add text first to isolate only the delete output
    app.do_add("TestDelete")
    captured = capsys.readouterr()

    app.do_delete("TestDelete")
    captured = capsys.readouterr()
    assert captured.out == "Successfully deleted class 'TestDelete'\n"

    #TODO
    #test do_list on the empty editor (rn it crashes the program)

def test_do_delete(capsys):

################################# TEST EDIT #################################

################################# ATTRIBUTES ################################
################################ TEST addAttr ###############################

################################ TEST delAttr ###############################

############################### TEST editAttr ###############################

############################### RELATIONSHIPS ###############################
################################ TEST addRel ################################

################################ TEST delRel ################################