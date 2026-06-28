from backend.services.trimmer.content_trimmer import ContentTrimmer

sample = """
Home

Support

Mac

Dell XPS 13

Processor
Intel Core Ultra 7

Battery
55 Wh

Privacy Policy

Shipping

Returns

16GB RAM

USB-C

Accessories

Buy Now
"""

trimmer = ContentTrimmer()

print(trimmer.trim(sample))