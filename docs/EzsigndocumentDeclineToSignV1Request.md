# EzsigndocumentDeclineToSignV1Request

Request for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/declineToSign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_reason** | **str** | Reason for refusal | 

## Example

```python
from eZmaxApi.models.ezsigndocument_decline_to_sign_v1_request import EzsigndocumentDeclineToSignV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentDeclineToSignV1Request from a JSON string
ezsigndocument_decline_to_sign_v1_request_instance = EzsigndocumentDeclineToSignV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentDeclineToSignV1Request.to_json()

# convert the object into a dict
ezsigndocument_decline_to_sign_v1_request_dict = ezsigndocument_decline_to_sign_v1_request_instance.to_dict()
# create an instance of EzsigndocumentDeclineToSignV1Request from a dict
ezsigndocument_decline_to_sign_v1_request_form_dict = ezsigndocument_decline_to_sign_v1_request.from_dict(ezsigndocument_decline_to_sign_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


