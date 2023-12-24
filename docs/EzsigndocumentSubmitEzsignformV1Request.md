# EzsigndocumentSubmitEzsignformV1Request

Request for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/submitEzsignform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_ezsignform_isdraft** | **bool** | Whether the Ezsignform submitted is a draft or not. | 
**a_obj_ezsignformfieldgroup** | [**List[CustomEzsignformfieldgroupRequest]**](CustomEzsignformfieldgroupRequest.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_submit_ezsignform_v1_request import EzsigndocumentSubmitEzsignformV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentSubmitEzsignformV1Request from a JSON string
ezsigndocument_submit_ezsignform_v1_request_instance = EzsigndocumentSubmitEzsignformV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentSubmitEzsignformV1Request.to_json()

# convert the object into a dict
ezsigndocument_submit_ezsignform_v1_request_dict = ezsigndocument_submit_ezsignform_v1_request_instance.to_dict()
# create an instance of EzsigndocumentSubmitEzsignformV1Request from a dict
ezsigndocument_submit_ezsignform_v1_request_form_dict = ezsigndocument_submit_ezsignform_v1_request.from_dict(ezsigndocument_submit_ezsignform_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


