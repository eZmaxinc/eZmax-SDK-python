# CustomEzsignformfielderrortestResponse

A Custom Ezsignformfielderrortest Object to contain the detail of the test error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezsignformfielderrortest_name** | **str** | The name of the test | 
**s_ezsignformfielderrortest_detail** | **str** | The detail why the test failed | 

## Example

```python
from eZmaxApi.models.custom_ezsignformfielderrortest_response import CustomEzsignformfielderrortestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignformfielderrortestResponse from a JSON string
custom_ezsignformfielderrortest_response_instance = CustomEzsignformfielderrortestResponse.from_json(json)
# print the JSON string representation of the object
print CustomEzsignformfielderrortestResponse.to_json()

# convert the object into a dict
custom_ezsignformfielderrortest_response_dict = custom_ezsignformfielderrortest_response_instance.to_dict()
# create an instance of CustomEzsignformfielderrortestResponse from a dict
custom_ezsignformfielderrortest_response_form_dict = custom_ezsignformfielderrortest_response.from_dict(custom_ezsignformfielderrortest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


