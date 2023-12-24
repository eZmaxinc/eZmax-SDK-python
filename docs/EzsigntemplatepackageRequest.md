# EzsigntemplatepackageRequest

A Ezsigntemplatepackage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_ezsigntemplatepackage_description** | **str** | The description of the Ezsigntemplatepackage | 
**b_ezsigntemplatepackage_adminonly** | **bool** | Whether the Ezsigntemplatepackage can be accessed by admin users only (eUserType&#x3D;Normal) | 
**b_ezsigntemplatepackage_isactive** | **bool** | Whether the Ezsigntemplatepackage is active or not | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_request import EzsigntemplatepackageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageRequest from a JSON string
ezsigntemplatepackage_request_instance = EzsigntemplatepackageRequest.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackageRequest.to_json()

# convert the object into a dict
ezsigntemplatepackage_request_dict = ezsigntemplatepackage_request_instance.to_dict()
# create an instance of EzsigntemplatepackageRequest from a dict
ezsigntemplatepackage_request_form_dict = ezsigntemplatepackage_request.from_dict(ezsigntemplatepackage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


