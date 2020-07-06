# coding=utf-8
import win32gui
import win32con

class FileuploadUtils(object):
    def upload_file(file_path):
        '''
        :param file_path:上传文件的路径
        :return:
        '''
        dialog = win32gui.FindWindow("#32770", "打开")
        comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
