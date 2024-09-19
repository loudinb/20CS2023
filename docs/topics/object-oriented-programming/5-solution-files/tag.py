class Tag:
    all_tags = {}

    def __init__(self, name):
        self.name = name
        self.post_count = 0

    @classmethod
    def get_or_create_tag(cls, name):
        if name not in cls.all_tags:
            cls.all_tags[name] = cls(name)
        return cls.all_tags[name]

    def increment_post_count(self):
        self.post_count += 1

    @staticmethod
    def get_trending_tags(limit=5):
        sorted_tags = sorted(Tag.all_tags.values(), key=lambda t: t.post_count, reverse=True)
        return sorted_tags[:limit]
