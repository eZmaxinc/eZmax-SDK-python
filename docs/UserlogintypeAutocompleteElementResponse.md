# UserlogintypeAutocompleteElementResponse

A Userlogintype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_userlogintype_id** | **int** | The unique ID of the Userlogintype  Valid values:  |Value|Description|Detail| |-|-|-| |1|**Email Only**|The Ezsignsigner will receive a secure link by email| |2|**Email and phone or SMS**|The Ezsignsigner will receive a secure link by email and will need to authenticate using SMS or Phone call. **Additional fee applies**| |3|**Email and secret question**|The Ezsignsigner will receive a secure link by email and will need to authenticate using a predefined question and answer| |4|**In person only**|The Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and there won&#39;t be any authentication. No email will be sent for invitation to sign. Make sure you evaluate the risk of signature denial and at minimum, we recommend you use a handwritten signature type| |5|**In person with phone or SMS**|The Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**| | 
**s_userlogintype_description_x** | **str** | The description of the Userlogintype in the language of the requester | 
**b_userlogintype_isactive** | **bool** | Whether the Userlogintype is active or not | 

## Example

```python
from eZmaxApi.models.userlogintype_autocomplete_element_response import UserlogintypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserlogintypeAutocompleteElementResponse from a JSON string
userlogintype_autocomplete_element_response_instance = UserlogintypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(UserlogintypeAutocompleteElementResponse.to_json())

# convert the object into a dict
userlogintype_autocomplete_element_response_dict = userlogintype_autocomplete_element_response_instance.to_dict()
# create an instance of UserlogintypeAutocompleteElementResponse from a dict
userlogintype_autocomplete_element_response_form_dict = userlogintype_autocomplete_element_response.from_dict(userlogintype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


