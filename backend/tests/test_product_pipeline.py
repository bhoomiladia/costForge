from backend.pipeline.product_pipeline import ProductPipeline

from backend.services.search.web_search_service import WebSearchService
from backend.services.search.providers.serper_provider import SerperProvider


def main():

    pipeline = ProductPipeline(
        search_service=WebSearchService(
            SerperProvider()
        )
    )

    specification = pipeline.run(
        "Dell XPS 13 specifications"
    )

    print("\n" + "=" * 80)
    print("FINAL SPECIFICATION")
    print("=" * 80)

    print(specification)

    print("\nProduct:", specification.product_name)
    print("Brand:", specification.brand)
    print("Processor:", specification.processor)
    print("Memory:", specification.memory)
    print("Storage:", specification.storage)
    print("Display:", specification.display)
    print("Battery:", specification.battery)
    print("Weight:", specification.weight)
    print("Ports:", specification.ports)
    print("Colors:", specification.colors)
    print("Special Features:", specification.special_features)


if __name__ == "__main__":
    main()