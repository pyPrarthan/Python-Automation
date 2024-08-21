import pywhatkit as pywhatkit

#Contact
phone_number = "+16478797231"  # Replace with a valid phone number including country code
message = "Hello from pywhatkit!"
hour = 14
minute = 21

pywhatkit.sendwhatmsg(phone_number, message, hour, minute, 15, True, 2) # type: ignore


#Group
group_id = input("Enter group id: ")
pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 7, 31) # type: ignore