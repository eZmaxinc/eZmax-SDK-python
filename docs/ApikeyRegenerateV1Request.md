# ApikeyRegenerateV1Request

Request for POST /1/object/apikey/{pkiApikeyID}/regenerate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_apikey_issigned** | **bool** | Whether the apikey is signed or not | [optional] 

## Example

```python
from eZmaxApi.models.apikey_regenerate_v1_request import ApikeyRegenerateV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyRegenerateV1Request from a JSON string
apikey_regenerate_v1_request_instance = ApikeyRegenerateV1Request.from_json(json)
# print the JSON string representation of the object
print(ApikeyRegenerateV1Request.to_json())

# convert the object into a dict
apikey_regenerate_v1_request_dict = apikey_regenerate_v1_request_instance.to_dict()
# create an instance of ApikeyRegenerateV1Request from a dict
apikey_regenerate_v1_request_from_dict = ApikeyRegenerateV1Request.from_dict(apikey_regenerate_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


