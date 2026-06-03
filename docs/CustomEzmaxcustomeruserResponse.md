# CustomEzmaxcustomeruserResponse

A Ezmaxcustomeruser Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezmaxcustomer** | [**CustomEzmaxcustomerResponse**](CustomEzmaxcustomerResponse.md) |  | 
**fki_contacttitle_id** | **int** | The unique ID of the Contacttitle.  Valid values:  |Value|Description| |-|-| |1|Ms.| |2|Mr.| |4|(Blank)| |5|Me (For Notaries)| | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**obj_email** | [**EmailResponseCompound**](EmailResponseCompound.md) |  | [optional] 
**obj_phone** | [**PhoneResponseCompound**](PhoneResponseCompound.md) |  | [optional] 
**s_ezmaxcustomeruser_firstname** | **str** | The First name of the Ezmaxcustomeruser | 
**s_ezmaxcustomeruser_lastname** | **str** | The First name of the Ezmaxcustomeruser | 

## Example

```python
from eZmaxApi.models.custom_ezmaxcustomeruser_response import CustomEzmaxcustomeruserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzmaxcustomeruserResponse from a JSON string
custom_ezmaxcustomeruser_response_instance = CustomEzmaxcustomeruserResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzmaxcustomeruserResponse.to_json())

# convert the object into a dict
custom_ezmaxcustomeruser_response_dict = custom_ezmaxcustomeruser_response_instance.to_dict()
# create an instance of CustomEzmaxcustomeruserResponse from a dict
custom_ezmaxcustomeruser_response_from_dict = CustomEzmaxcustomeruserResponse.from_dict(custom_ezmaxcustomeruser_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


