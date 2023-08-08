from sqlalchemy import Column, Integer, String, DateTime

from server.db.base import Base


class KnowledgeBaseModel(Base):
    """
    知识库模型
    """
    __tablename__ = 'knowledge_base'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='知识库ID')
    kb_name = Column(String, comment='知识库名称')
    vs_type = Column(String, comment='嵌入模型类型')
    embed_model = Column(String, comment='嵌入模型名称')
    file_count = Column(Integer, comment='文件数量')
    create_time = Column(DateTime, comment='创建时间')

    def __repr__(self):
        return f"<KnowledgeBase(id='{self.id}', kb_name='{self.kb_name}', vs_type='{self.vs_type}', embed_model='{self.embed_model}', file_count='{self.file_count}', create_time='{self.create_time}')>"
