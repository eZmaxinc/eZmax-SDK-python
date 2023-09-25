# EzsigntemplateRequest

A Ezsigntemplate Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_ezsigntemplate_description** | **str** | The description of the Ezsigntemplate | 
**b_ezsigntemplate_adminonly** | **bool** | Whether the Ezsigntemplate can be accessed by admin users only (eUserType&#x3D;Normal) | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_request import EzsigntemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateRequest from a JSON string
ezsigntemplate_request_instance = EzsigntemplateRequest.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateRequest.to_json()

# convert the object into a dict
ezsigntemplate_request_dict = ezsigntemplate_request_instance.to_dict()
# create an instance of EzsigntemplateRequest from a dict
ezsigntemplate_request_form_dict = ezsigntemplate_request.from_dict(ezsigntemplate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


