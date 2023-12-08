import graphene
from restapi.models import Me, Project, Pricing, Skill, Contact

from .modeltypes import(
    MeType,
    ProjectType,
    PricingType,
    SkillType,
    ContactType,
)

#GET = query

class Query(graphene.ObjectType):
    me = graphene.List(MeType)
    projects = graphene.List(ProjectType)
    pricing = graphene.List(PricingType)
    skills = graphene.List(SkillType)
    contacts = graphene.List(ContactType)
    
    def resolve_me(self, info):
        return Me.objects.all()
    
    def resolve_projects(self, info):
        return Project.objects.all()
    
    def resolve_pricing(self, info):
        return Pricing.objects.all()
    
    def resolve_skills(self, info):
        return Skill.objects.all()
    
    def resolve_contacts(self, info):
        return Contact.objects.all()
