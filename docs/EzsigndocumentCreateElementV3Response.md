# EzsigndocumentCreateElementV3Response

A Ezsigndocument createObject Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**a_obj_matchingtemplate** | [**List[EzsigndocumentMatchingtemplateV3Response]**](EzsigndocumentMatchingtemplateV3Response.md) | An array of possibly matching template. | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_element_v3_response import EzsigndocumentCreateElementV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateElementV3Response from a JSON string
ezsigndocument_create_element_v3_response_instance = EzsigndocumentCreateElementV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentCreateElementV3Response.to_json())

# convert the object into a dict
ezsigndocument_create_element_v3_response_dict = ezsigndocument_create_element_v3_response_instance.to_dict()
# create an instance of EzsigndocumentCreateElementV3Response from a dict
ezsigndocument_create_element_v3_response_from_dict = EzsigndocumentCreateElementV3Response.from_dict(ezsigndocument_create_element_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


