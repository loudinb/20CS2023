class Tag:
    all_tags = {}

    def __init__(self, name: str):
        self.name = name
        self.usage_count = 0

    @classmethod
    def get_or_create(cls, tag_name: str) -> 'Tag':
        if tag_name not in cls.all_tags:
            cls.all_tags[tag_name] = cls(tag_name)
        return cls.all_tags[tag_name]

    def increment_usage(self) -> None:
        self.usage_count += 1

    @staticmethod
    def get_trending_tags(top_n: int = 5) -> list:
        return sorted(Tag.all_tags.values(), key=lambda t: t.usage_count, reverse=True)[:top_n]
