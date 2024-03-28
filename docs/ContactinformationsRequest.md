# ContactinformationsRequest

A Contactinformations Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_address_default** | **int** | The index in the a_objAddress array (zero based index) representing the Address object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**i_phone_default** | **int** | The index in the a_objPhone array (zero based index) representing the Phone object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**i_email_default** | **int** | The index in the a_objEmail array (zero based index) representing the Email object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**i_website_default** | **int** | The index in the a_objWebsite array (zero based index) representing the Website object that should become the default one.  You can leave the value to 0 if the array is empty. | 

## Example

```python
from eZmaxApi.models.contactinformations_request import ContactinformationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContactinformationsRequest from a JSON string
contactinformations_request_instance = ContactinformationsRequest.from_json(json)
# print the JSON string representation of the object
print(ContactinformationsRequest.to_json())

# convert the object into a dict
contactinformations_request_dict = contactinformations_request_instance.to_dict()
# create an instance of ContactinformationsRequest from a dict
contactinformations_request_form_dict = contactinformations_request.from_dict(contactinformations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


