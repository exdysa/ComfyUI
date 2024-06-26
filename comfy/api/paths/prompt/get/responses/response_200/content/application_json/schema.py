# coding: utf-8

"""
    comfyui
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from comfy.api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

QueueRemaining: typing_extensions.TypeAlias = schemas.IntSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "queue_remaining": typing.Type[QueueRemaining],
    }
)


class ExecInfoDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "queue_remaining",
    })
    
    def __new__(
        cls,
        *,
        queue_remaining: typing.Union[
            int,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("queue_remaining", queue_remaining),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(ExecInfoDictInput, arg_)
        return ExecInfo.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            ExecInfoDictInput,
            ExecInfoDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ExecInfoDict:
        return ExecInfo.validate(arg, configuration=configuration)
    
    @property
    def queue_remaining(self) -> typing.Union[int, schemas.Unset]:
        val = self.get("queue_remaining", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            int,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
ExecInfoDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ExecInfo(
    schemas.Schema[ExecInfoDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ExecInfoDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ExecInfoDictInput,
            ExecInfoDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ExecInfoDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

Properties2 = typing.TypedDict(
    'Properties2',
    {
        "exec_info": typing.Type[ExecInfo],
    }
)


class SchemaDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "exec_info",
    })
    
    def __new__(
        cls,
        *,
        exec_info: typing.Union[
            ExecInfoDictInput,
            ExecInfoDict,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("exec_info", exec_info),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(SchemaDictInput, arg_)
        return Schema.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            SchemaDictInput,
            SchemaDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SchemaDict:
        return Schema.validate(arg, configuration=configuration)
    
    @property
    def exec_info(self) -> typing.Union[ExecInfoDict, schemas.Unset]:
        val = self.get("exec_info", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            ExecInfoDict,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
SchemaDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class Schema(
    schemas.Schema[SchemaDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties2 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties2)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: SchemaDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            SchemaDictInput,
            SchemaDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SchemaDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

