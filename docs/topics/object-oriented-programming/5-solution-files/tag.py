class Tag:
    all_tags = {}

    def __init__(self, name):
        self.name = name.lower()
        self.posts = []

    @classmethod
    def get_or_create(cls, name):
        name = name.lower()
        if name not in cls.all_tags:
            cls.all_tags[name] = cls(name)
        return cls.all_tags[name]

    def add_post(self, post):
        if post not in self.posts:
            self.posts.append(post)

    @staticmethod
    def get_trending_tags(limit=5):
        sorted_tags = sorted(Tag.all_tags.values(), key=lambda t: len(t.posts), reverse=True)
        return sorted_tags[:limit]

    @classmethod
    def get_all_tags(cls):
        return list(cls.all_tags.values())
