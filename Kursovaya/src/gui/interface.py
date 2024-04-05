from tkinter import *
class Enums:
    class StatusEnum:
        ENABLED = 0
        DISABLED = 1

class PageProperties:
    
    tag = ""
    size = {
        'width': 600, 
        'height': 1000
        }
    status = Enums.StatusEnum.DISABLED

    def __init__(self, pageTag, width = 600, height = 1000, status = Enums.StatusEnum.DISABLED):
        self.tag = str(pageTag)
        self.size = {"width":int(width), "height":int(height)}
        self.status = str(status)
    
    #tags:
        #"page_booking"
        #"page_contact"
        #"page_description"

    @property
    def get_id(self):
        return self.tag

    @tag.setter
    def set_id(self, newTag):
        self.tag = str(newTag)

    @property
    def get_size(self):
        return self.size
    
    @size.setter
    def set_size(self, width = get_size().width, height = get_size().height, dictSize = get_size()):
        self.size = dictSize
        self.size.width = width
        self.size.height = height

    @property
    def get_status(self):
        return self.status
    
    @status.setter
    def set_status(self, newStatus):
        self._changeStatus(self, newStatus)
        
    def _changeStatus(self, newStatus):
        self.status = newStatus
        #спрятать страницу
        pass


class Page:
    #   Menu
    #|-Image Restaraunt_Name_Text
    #|  |-Button
    #|     |-page_description
    #|-Image Booking_Text
    #|  |-Button
    #|     |-page_booking
    #|-Image Contact_Us_Text
    #|  |-Button
    #|     |-page_contact

    def __init__(self):
        self.root = Tk()
        self.root.geometry(f"{self.size['width']}x{self.size['height']}")
        pass
    

    class Header:
        def __init__(self):
            pass

    #Page filling
    class Body:
        def __init__(self):
            pass

