from pyscript import display, document

# clubs dictionary 
club_information = {
    "Science Club":{
        'Name':'Science Club',
        'Description':'A club for those who loves experiments',
        'Meeting Time':'Monday and Friday, 3:30-4:30',
        'Location':'420',
        'Category':'Academic'
    },

    "Math Club":{
        'Name':'Math Club',
        'Description':'A club that students love problem-solving, and competitions',
        'Meeting Time':'Tuesday and Wednesday, 4:00-5:30',
        'Location':'510',
        'Category':'Academic'
    },

    "Debate Club":{
        'Name':'Debate Club',
        'Description':'A club for those who love to agrue',
        'Meeting Time':'Thrusday and Friday, 2:30:00-4:30',
        'Location':'Room 610',
        'Category':'Academic'
    }
}

def clubdetails(e): # function gets data from dropdown, to then display

    values = document.getElementById('cluboptions').value 
    data_display = club_information[values]
    document.getElementById("output").innerHTML = ""

    display(f"{values}", target="output")
    display(f"Description: {data_display['Description']}", target="output")
    display(f"Meeting Time: {data_display['Meeting Time']}", target="output")
    display(f"Location: {data_display['Location']}", target="output")
    display(f"Category: {data_display['Category']}", target="output")
   

    

   