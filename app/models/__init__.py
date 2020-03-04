# from .. import db

# class Caption(db.Model):
#     __tablename__   = 'caption'
#     id              = db.Column(db.Integer, primary_key=True)
#     title           = db.Column(db.Text)

#     tag_group_id    = db.Column(db.Integer, db.ForeignKey('caption_tag_group.id'))
#     tag_group       = db.relationship('CaptionTagGroup', back_populates='captions')

#     customs         = db.relationship('Custom', back_populates='caption')
#     url             = db.Column(db.Text)

#     def __init__(self, title=None, url=None, tag_names=[]):
#         self.tag_group      = find_or_create(CaptionTagGroup, tag_names)
#         self.tag_group_id   = self.tag_group.id
#         self.title          = title
#         self.url            = url

#     def __repr__(self):
#         return '{} {}'.format(self.title, [tag.name for tag in self.tag_group.tags])