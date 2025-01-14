# EzsigndocumentMatchingtemplateV3Response

A Ezsigndocument createObject Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | [optional] 
**pki_ezsigntemplateglobal_id** | **int** | The unique ID of the Ezsigntemplateglobal | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_matchingtemplate_v3_response import EzsigndocumentMatchingtemplateV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentMatchingtemplateV3Response from a JSON string
ezsigndocument_matchingtemplate_v3_response_instance = EzsigndocumentMatchingtemplateV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentMatchingtemplateV3Response.to_json())

# convert the object into a dict
ezsigndocument_matchingtemplate_v3_response_dict = ezsigndocument_matchingtemplate_v3_response_instance.to_dict()
# create an instance of EzsigndocumentMatchingtemplateV3Response from a dict
ezsigndocument_matchingtemplate_v3_response_from_dict = EzsigndocumentMatchingtemplateV3Response.from_dict(ezsigndocument_matchingtemplate_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


