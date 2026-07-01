from typing import get_origin

from backend.models.product_specifications import ProductSpecifications


class SpecificationMerger:
    """
    Merges multiple ProductSpecifications into a single object.
    """

    def merge(
        self,
        specifications: list[ProductSpecifications],
    ) -> ProductSpecifications:
        """
        Merge multiple ProductSpecifications.
        """

        if not specifications:
            raise ValueError(
                "No specifications provided."
            )

        merged = specifications[0].model_copy(deep=True)

        for specification in specifications[1:]:
            self._merge_into(
                merged,
                specification,
            )

        return merged

    def _merge_into(
        self,
        target: ProductSpecifications,
        source: ProductSpecifications,
    ) -> None:
        """
        Merge one ProductSpecifications object into another.
        """

        for field_name, field_info in ProductSpecifications.model_fields.items():

            target_value = getattr(
                target,
                field_name,
            )

            source_value = getattr(
                source,
                field_name,
            )

            annotation = field_info.annotation

            if self._is_list_field(annotation):

                self._merge_list(
                    target,
                    field_name,
                    target_value,
                    source_value,
                )

            else:

                self._merge_scalar(
                    target,
                    field_name,
                    target_value,
                    source_value,
                )

    def _merge_scalar(
        self,
        target: ProductSpecifications,
        field_name: str,
        target_value,
        source_value,
    ) -> None:
        """
        Merge scalar values.

        Strategy:
        - Keep the first meaningful value.
        - Ignore None and empty strings.
        """

        if self._is_empty(target_value) and not self._is_empty(source_value):

            setattr(
                target,
                field_name,
                source_value,
            )

    def _merge_list(
        self,
        target: ProductSpecifications,
        field_name: str,
        target_value,
        source_value,
    ) -> None:
        """
        Merge list fields.

        Strategy:
        - Combine both lists.
        - Remove duplicates.
        - Preserve insertion order.
        """

        target_list = target_value or []
        source_list = source_value or []

        merged_list = list(
            dict.fromkeys(
                target_list + source_list
            )
        )

        if merged_list != target_list:

            setattr(
                target,
                field_name,
                merged_list,
            )

    def _is_empty(
        self,
        value,
    ) -> bool:
        """
        Check whether a scalar value is empty.
        """

        return value is None or value == ""

    def _is_list_field(
        self,
        annotation,
    ) -> bool:
        """
        Determine whether a field is a list.
        """

        origin = get_origin(annotation)

        return origin is list