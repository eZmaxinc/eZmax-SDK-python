# EzsigntemplateCreateObjectV2Request

Request for POST /2/object/ezsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplate** | [**List[EzsigntemplateRequestCompoundV2]**](EzsigntemplateRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_create_object_v2_request import EzsigntemplateCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateCreateObjectV2Request from a JSON string
ezsigntemplate_create_object_v2_request_instance = EzsigntemplateCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateCreateObjectV2Request.to_json())

# convert the object into a dict
ezsigntemplate_create_object_v2_request_dict = ezsigntemplate_create_object_v2_request_instance.to_dict()
# create an instance of EzsigntemplateCreateObjectV2Request from a dict
ezsigntemplate_create_object_v2_request_form_dict = ezsigntemplate_create_object_v2_request.from_dict(ezsigntemplate_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


