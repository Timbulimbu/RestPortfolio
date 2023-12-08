# DELETE, UPDATE, POST = mutations
# create, update, delete mutations



import graphene
from graphql import GraphQLError

from restapi.models import Me, Project, Pricing, Skill, Contact

from .modeltypes import(
    MeType,
    ProjectType,
    PricingType,
    SkillType,
    ContactType,
)

class CreateMe(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        instagram =graphene.String()
        github = graphene.String()
        linkedin = graphene.String()
        telegram = graphene.String()
        education = graphene.String()
        work_history = graphene.String()
        
    me = graphene.Field(MeType)
    
    def mutate(self, info, first_name, last_name, email, phone, **kwargs):
        me = Me.objects.create(**kwargs)
        me.save()
        return CreateMe(me=me)


class UpdateMe(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        instagram =graphene.String()
        github = graphene.String()
        linkedin = graphene.String()
        telegram = graphene.String()
        education = graphene.String()
        work_history = graphene.String()
        
    me = graphene.Field(MeType)
    
    def mutate(self, info, id, **kwargs):
        try:
            me = Me.objects.get(id=id)
        except Me.DoesNotExist:
            raise GraphQLError(f"Информация о пользователе с {id} отсутствует")
            
            
        me.first_name = kwargs.get('first_name', me.first_name)
        me.last_name = kwargs.get('last_name', me.last_name)
        me.email = kwargs.get('email', me.email)
        me.phone = kwargs.get('phone', me.phone)
        me.instagram = kwargs.get('instagram', me.instagram)
        me.github = kwargs.get('github', me.github)
        me.linkedin = kwargs.get('linkedin', me.linkedin)
        me.telegram = kwargs.get('telegram', me.telegram)
        me.education = kwargs.get('education', me.education)
        me.work_history = kwargs.get('work_history', me.work_history)

        me.save()
        return UpdateMe(me=me)

class DeleteMe(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            me = Me.objects.get(id=id)
        except Me.DoesNotExist:
            raise GraphQLError(f"Информация о пользователе с id={id} отсутствует")
            
        me.delete()
        return DeleteMe(success=True)  

    
    
class CreateProject(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        url= graphene.String()
        repository = graphene.String()
        technologies_used = graphene.String()
        file = graphene.String()
        image = graphene.String()
        start_date = graphene.Date(required=True)
        end_date = graphene.Date()
        
             
    project = graphene.Field(ProjectType)
    
    def mutate(self, info, title, description, start_date, **kwargs):
        
        project = Project(
            title=title,
            description=description,
            start_date=start_date,
            url = kwargs.get('url'),
            repository = kwargs.get('repository'),
            technologies_used = kwargs.get('technologies_used'),
            file = kwargs.get('file'),
            image = kwargs.get('image'),
            end_date = kwargs.get('end_date'),
      
        )
        project.save()
        return CreateProject(project=project)

class UpdateProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        url= graphene.String()
        repository = graphene.String()
        technologies_used = graphene.String()
        file = graphene.String()
        image = graphene.String()
        start_date = graphene.Date()
        end_date = graphene.Date()
        
             
    project = graphene.Field(ProjectType)
    
    def mutate(self, info, id, **kwargs):
        try:
            project = Project.objects.get(pk=id)
        except Project.DoesNotExist:
            raise GraphQLError(f"Информация о проекте с id={id} отсутствует")
            
        project.title = kwargs.get('title', project.title)
        project.description = kwargs.get('description', project.description)
        project.url = kwargs.get('url', project.url)
        project.repository = kwargs.get('repository', project.repository)
        project.technologies_used = kwargs.get('technologies_used', project.technologies_used)
        project.file = kwargs.get('file', project.file)
        project.image = kwargs.get('image', project.image)
        project.start_date = kwargs.get('start_date', project.start_date)
        project.end_date = kwargs.get('end_date', project.end_date)
        
        project.save()
        return UpdateProject(project=project)

class DeleteProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            project = Project.objects.get(pk=id)
        except Project.DoesNotExist:
            raise GraphQLError(f"Информация о проекте с id={id} отсутствует")
            
        project.delete()
        return DeleteProject(success=True)
    
    
class CreatePricing(graphene.Mutation):
    class Arguments:
        service = graphene.String(required=True)
        description = graphene.String(required=True)
        rate_per_hour = graphene.Decimal(required=True)
        estimated_time = graphene.Decimal(required=True)
        
    pricing = graphene.Field(PricingType)
    
    def mutate(self, info, service, description, rate_per_hour, estimated_time):
        pricing = Pricing(
            service=service,
            description=description,
            rate_per_hour=rate_per_hour,
            estimated_time=estimated_time,
        )
        pricing.save()
        return CreatePricing(pricing=pricing)
    
class UpdatePricing(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        service = graphene.String()
        description = graphene.String()
        rate_per_hour = graphene.Decimal()
        estimated_time = graphene.Decimal()
        
    pricing = graphene.Field(PricingType)
    
    def mutate(self, info, id, **kwargs):
        try:
            pricing = Pricing.objects.get(pk=id)
        except Pricing.DoesNotExist:
            raise GraphQLError(f"Информация о расценке с id={id} отсутствует")
            
        pricing.service = kwargs.get('service', pricing.service)
        pricing.description = kwargs.get('description', pricing.description)
        pricing.rate_per_hour = kwargs.get('rate_per_hour', pricing.rate_per_hour)
        pricing.estimated_time = kwargs.get('estimated_time', pricing.estimated_time)
        
        pricing.save()
        return UpdatePricing(pricing=pricing)

class DeletePricing(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            pricing = Pricing.objects.get(pk=id)
        except Pricing.DoesNotExist:
            raise GraphQLError(f"Информация о расценке с id={id} отсутствует")
            
        pricing.delete()
        return DeletePricing(success=True)
    

class CreateSkill(graphene.Mutation):
    class Arguments:
        category = graphene.String(required=True)
        name = graphene.String(required=True)
        percentage = graphene.Int(required=True)
    
    skill = graphene.Field(SkillType)
    
    def mutate(self, info, category, name, percentage):
        skill = Skill(
            category=category,
            name=name,
            percentage=percentage,
        )
        skill.save()
        return CreateSkill(skill=skill) 
    
class UpdateSkill(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        category = graphene.String()
        name = graphene.String()
        percentage = graphene.Int()
        
    skill = graphene.Field(SkillType)
    
    def mutate(self, info, id, **kwargs):
        try:
            skill = Skill.objects.get(pk=id)
        except Skill.DoesNotExist:
            raise GraphQLError(f"Информация о навыке с id={id} отсутствует")
            
        skill.category = kwargs.get('category', skill.category)
        skill.name = kwargs.get('name', skill.name)
        skill.percentage = kwargs.get('percentage', skill.percentage)
        
        skill.save()
        return UpdateSkill(skill=skill)
    
class DeleteSkill(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            skill = Skill.objects.get(pk=id)
        except Skill.DoesNotExist:
            raise GraphQLError(f"Информация о навыке с id={id} отсутствует")
            
        skill.delete()
        return DeleteSkill(success=True)
    
class CreateContact(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        subject = graphene.String(required=True)
        message = graphene.String(required=True)    
    
    contact = graphene.Field(ContactType)
    
    def mutate(self, info, name, email, subject, message):
        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact.save()
        return CreateContact(contact=contact)
    
class UpdateContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()
        subject = graphene.String()
        message = graphene.String()
        
    contact = graphene.Field(ContactType)
    
    def mutate(self, info, id, **kwargs):
        try:
            contact = Contact.objects.get(pk=id)
        except Contact.DoesNotExist:
            raise GraphQLError(f"Информация о контакте с id={id} отсутствует")
            
        contact.name = kwargs.get('name', contact.name)
        contact.email = kwargs.get('email', contact.email)
        contact.subject = kwargs.get('subject', contact.subject)
        contact.message = kwargs.get('message', contact.message)
        
        contact.save()
        return UpdateContact(contact=contact)
    
class DeleteContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            contact = Contact.objects.get(pk=id)
        except Contact.DoesNotExist:
            raise GraphQLError(f"Информация о контакте с id={id} отсутствует")
            
        contact.delete()
        return DeleteContact(success=True)
    
    
class Mutation(graphene.ObjectType):
    create_me = CreateMe.Field()
    update_me = UpdateMe.Field()
    delete_me = DeleteMe.Field()
    
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()
    
    create_pricing = CreatePricing.Field()
    update_pricing = UpdatePricing.Field()
    delete_pricing = DeletePricing.Field()
    
    create_skill = CreateSkill.Field()
    update_skill = UpdateSkill.Field()
    delete_skill = DeleteSkill.Field()
    
    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()
    delete_contact = DeleteContact.Field()
