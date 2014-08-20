# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'dashboard_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'dashboard', ['Country'])

        # Adding model 'UserCountry'
        db.create_table(u'dashboard_usercountry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
        ))
        db.send_create_signal(u'dashboard', ['UserCountry'])

        # Adding model 'Period'
        db.create_table(u'dashboard_period', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('end_year', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'dashboard', ['Period'])

        # Adding model 'PriorityArea'
        db.create_table(u'dashboard_priorityarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'dashboard', ['PriorityArea'])

        # Adding unique constraint on 'PriorityArea', fields ['country', 'name']
        db.create_unique(u'dashboard_priorityarea', ['country_id', 'name'])

        # Adding model 'SectorCategory'
        db.create_table(u'dashboard_sectorcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'dashboard', ['SectorCategory'])

        # Adding model 'TenderProcedureProperty'
        db.create_table(u'dashboard_tenderprocedureproperty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sector_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.SectorCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'dashboard', ['TenderProcedureProperty'])

        # Adding unique constraint on 'TenderProcedureProperty', fields ['sector_category', 'name']
        db.create_unique(u'dashboard_tenderprocedureproperty', ['sector_category_id', 'name'])

        # Adding model 'Technology'
        db.create_table(u'dashboard_technology', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility_character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.FacilityCharacter'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'dashboard', ['Technology'])

        # Adding unique constraint on 'Technology', fields ['facility_character', 'name']
        db.create_unique(u'dashboard_technology', ['facility_character_id', 'name'])

        # Adding model 'FacilityCharacter'
        db.create_table(u'dashboard_facilitycharacter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sector_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.SectorCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'dashboard', ['FacilityCharacter'])

        # Adding unique constraint on 'FacilityCharacter', fields ['sector_category', 'name']
        db.create_unique(u'dashboard_facilitycharacter', ['sector_category_id', 'name'])

        # Adding model 'CommunityApproachType'
        db.create_table(u'dashboard_communityapproachtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'dashboard', ['CommunityApproachType'])

        # Adding model 'Partner'
        db.create_table(u'dashboard_partner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('mission', self.gf('django.db.models.fields.TextField')()),
            ('key_activities', self.gf('django.db.models.fields.TextField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'dashboard', ['Partner'])

        # Adding model 'Event'
        db.create_table(u'dashboard_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('venue', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'dashboard', ['Event'])

        # Adding model 'CountryDemographic'
        db.create_table(u'dashboard_countrydemographic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Period'])),
            ('population', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'dashboard', ['CountryDemographic'])

        # Adding unique constraint on 'CountryDemographic', fields ['country', 'year']
        db.create_unique(u'dashboard_countrydemographic', ['country_id', 'year_id'])

        # Adding model 'PriorityAreaStatus'
        db.create_table(u'dashboard_priorityareastatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority_area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PriorityArea'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Period'])),
            ('population', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('number_of_households', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'dashboard', ['PriorityAreaStatus'])

        # Adding unique constraint on 'PriorityAreaStatus', fields ['priority_area', 'year']
        db.create_unique(u'dashboard_priorityareastatus', ['priority_area_id', 'year_id'])

        # Adding model 'FacilityAccess'
        db.create_table(u'dashboard_facilityaccess', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority_area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PriorityArea'])),
            ('technology', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Technology'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Period'])),
            ('planned', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('planned_pop_affected', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('actual', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('actual_pop_affected', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('secured', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('secured_pop_affected', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('unit_cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=19, decimal_places=2, blank=True)),
            ('house_hold_contribution', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('government_contribution', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['FacilityAccess'])

        # Adding unique constraint on 'FacilityAccess', fields ['priority_area', 'technology', 'year']
        db.create_unique(u'dashboard_facilityaccess', ['priority_area_id', 'technology_id', 'year_id'])

        # Adding model 'SectorPerformance'
        db.create_table(u'dashboard_sectorperformance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
            ('sector_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.SectorCategory'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Period'])),
            ('coverage_target', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('coverage_achieved', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('fund_needed', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('fund_mobilised', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('fund_availed', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('fund_used', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('general_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bottlenecks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('measures_taken', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('success_challenges', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['SectorPerformance'])

        # Adding unique constraint on 'SectorPerformance', fields ['country', 'sector_category', 'year']
        db.create_unique(u'dashboard_sectorperformance', ['country_id', 'sector_category_id', 'year_id'])

        # Adding model 'PlanningPerformance'
        db.create_table(u'dashboard_planningperformance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
            ('sector_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.SectorCategory'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Period'])),
            ('plan_preparation_delay', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('plan_adoption_delay', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('general_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bottlenecks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('measures_taken', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('success_challenges', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['PlanningPerformance'])

        # Adding unique constraint on 'PlanningPerformance', fields ['country', 'sector_category', 'year']
        db.create_unique(u'dashboard_planningperformance', ['country_id', 'sector_category_id', 'year_id'])

        # Adding model 'TenderProcedurePerformance'
        db.create_table(u'dashboard_tenderprocedureperformance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Period'])),
            ('tender_procedure_property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.TenderProcedureProperty'])),
            ('registered', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('executed', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('general_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bottlenecks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('measures_taken', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('success_challenges', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['TenderProcedurePerformance'])

        # Adding unique constraint on 'TenderProcedurePerformance', fields ['country', 'tender_procedure_property', 'year']
        db.create_unique(u'dashboard_tenderprocedureperformance', ['country_id', 'tender_procedure_property_id', 'year_id'])

        # Adding model 'CommunityApproach'
        db.create_table(u'dashboard_communityapproach', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
            ('sector_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.SectorCategory'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Period'])),
            ('approach_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.CommunityApproachType'])),
            ('approach_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cost_per_capita', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('lessons_learnt', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CommunityApproach'])

        # Adding unique constraint on 'CommunityApproach', fields ['country', 'sector_category', 'year']
        db.create_unique(u'dashboard_communityapproach', ['country_id', 'sector_category_id', 'year_id'])

        # Adding model 'PartnerContribution'
        db.create_table(u'dashboard_partnercontribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
            ('sector_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.SectorCategory'])),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Partner'])),
            ('annual_contribution', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=4, blank=True)),
            ('in_kind_contribution', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('financial_contribution', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['PartnerContribution'])

        # Adding unique constraint on 'PartnerContribution', fields ['country', 'sector_category', 'partner']
        db.create_unique(u'dashboard_partnercontribution', ['country_id', 'sector_category_id', 'partner_id'])

        # Adding model 'PartnerEventContribution'
        db.create_table(u'dashboard_partnereventcontribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
            ('sector_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.SectorCategory'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Period'])),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Partner'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Event'])),
            ('government_staff_contribution', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('own_staff_contribution', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['PartnerEventContribution'])

        # Adding unique constraint on 'PartnerEventContribution', fields ['country', 'sector_category', 'year']
        db.create_unique(u'dashboard_partnereventcontribution', ['country_id', 'sector_category_id', 'year_id'])

        # Adding model 'SWOT'
        db.create_table(u'dashboard_swot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Country'])),
            ('sector_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.SectorCategory'])),
            ('overall_challenges', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('strengths', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('weaknesses', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('opportunities', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('risks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mitigation_measures', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('kap_recommendations', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('conclusion', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['SWOT'])


    def backwards(self, orm):
        # Removing unique constraint on 'PartnerEventContribution', fields ['country', 'sector_category', 'year']
        db.delete_unique(u'dashboard_partnereventcontribution', ['country_id', 'sector_category_id', 'year_id'])

        # Removing unique constraint on 'PartnerContribution', fields ['country', 'sector_category', 'partner']
        db.delete_unique(u'dashboard_partnercontribution', ['country_id', 'sector_category_id', 'partner_id'])

        # Removing unique constraint on 'CommunityApproach', fields ['country', 'sector_category', 'year']
        db.delete_unique(u'dashboard_communityapproach', ['country_id', 'sector_category_id', 'year_id'])

        # Removing unique constraint on 'TenderProcedurePerformance', fields ['country', 'tender_procedure_property', 'year']
        db.delete_unique(u'dashboard_tenderprocedureperformance', ['country_id', 'tender_procedure_property_id', 'year_id'])

        # Removing unique constraint on 'PlanningPerformance', fields ['country', 'sector_category', 'year']
        db.delete_unique(u'dashboard_planningperformance', ['country_id', 'sector_category_id', 'year_id'])

        # Removing unique constraint on 'SectorPerformance', fields ['country', 'sector_category', 'year']
        db.delete_unique(u'dashboard_sectorperformance', ['country_id', 'sector_category_id', 'year_id'])

        # Removing unique constraint on 'FacilityAccess', fields ['priority_area', 'technology', 'year']
        db.delete_unique(u'dashboard_facilityaccess', ['priority_area_id', 'technology_id', 'year_id'])

        # Removing unique constraint on 'PriorityAreaStatus', fields ['priority_area', 'year']
        db.delete_unique(u'dashboard_priorityareastatus', ['priority_area_id', 'year_id'])

        # Removing unique constraint on 'CountryDemographic', fields ['country', 'year']
        db.delete_unique(u'dashboard_countrydemographic', ['country_id', 'year_id'])

        # Removing unique constraint on 'FacilityCharacter', fields ['sector_category', 'name']
        db.delete_unique(u'dashboard_facilitycharacter', ['sector_category_id', 'name'])

        # Removing unique constraint on 'Technology', fields ['facility_character', 'name']
        db.delete_unique(u'dashboard_technology', ['facility_character_id', 'name'])

        # Removing unique constraint on 'TenderProcedureProperty', fields ['sector_category', 'name']
        db.delete_unique(u'dashboard_tenderprocedureproperty', ['sector_category_id', 'name'])

        # Removing unique constraint on 'PriorityArea', fields ['country', 'name']
        db.delete_unique(u'dashboard_priorityarea', ['country_id', 'name'])

        # Deleting model 'Country'
        db.delete_table(u'dashboard_country')

        # Deleting model 'UserCountry'
        db.delete_table(u'dashboard_usercountry')

        # Deleting model 'Period'
        db.delete_table(u'dashboard_period')

        # Deleting model 'PriorityArea'
        db.delete_table(u'dashboard_priorityarea')

        # Deleting model 'SectorCategory'
        db.delete_table(u'dashboard_sectorcategory')

        # Deleting model 'TenderProcedureProperty'
        db.delete_table(u'dashboard_tenderprocedureproperty')

        # Deleting model 'Technology'
        db.delete_table(u'dashboard_technology')

        # Deleting model 'FacilityCharacter'
        db.delete_table(u'dashboard_facilitycharacter')

        # Deleting model 'CommunityApproachType'
        db.delete_table(u'dashboard_communityapproachtype')

        # Deleting model 'Partner'
        db.delete_table(u'dashboard_partner')

        # Deleting model 'Event'
        db.delete_table(u'dashboard_event')

        # Deleting model 'CountryDemographic'
        db.delete_table(u'dashboard_countrydemographic')

        # Deleting model 'PriorityAreaStatus'
        db.delete_table(u'dashboard_priorityareastatus')

        # Deleting model 'FacilityAccess'
        db.delete_table(u'dashboard_facilityaccess')

        # Deleting model 'SectorPerformance'
        db.delete_table(u'dashboard_sectorperformance')

        # Deleting model 'PlanningPerformance'
        db.delete_table(u'dashboard_planningperformance')

        # Deleting model 'TenderProcedurePerformance'
        db.delete_table(u'dashboard_tenderprocedureperformance')

        # Deleting model 'CommunityApproach'
        db.delete_table(u'dashboard_communityapproach')

        # Deleting model 'PartnerContribution'
        db.delete_table(u'dashboard_partnercontribution')

        # Deleting model 'PartnerEventContribution'
        db.delete_table(u'dashboard_partnereventcontribution')

        # Deleting model 'SWOT'
        db.delete_table(u'dashboard_swot')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dashboard.communityapproach': {
            'Meta': {'unique_together': "(('country', 'sector_category', 'year'),)", 'object_name': 'CommunityApproach'},
            'approach_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'approach_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.CommunityApproachType']"}),
            'cost_per_capita': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons_learnt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sector_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.SectorCategory']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Period']"})
        },
        u'dashboard.communityapproachtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'CommunityApproachType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        u'dashboard.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'dashboard.countrydemographic': {
            'Meta': {'unique_together': "(('country', 'year'),)", 'object_name': 'CountryDemographic'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Period']"})
        },
        u'dashboard.event': {
            'Meta': {'ordering': "['name']", 'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'dashboard.facilityaccess': {
            'Meta': {'unique_together': "(('priority_area', 'technology', 'year'),)", 'object_name': 'FacilityAccess'},
            'actual': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'actual_pop_affected': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'government_contribution': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'house_hold_contribution': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'planned': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planned_pop_affected': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'priority_area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PriorityArea']"}),
            'secured': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'secured_pop_affected': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'technology': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Technology']"}),
            'unit_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2', 'blank': 'True'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Period']"})
        },
        u'dashboard.facilitycharacter': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('sector_category', 'name'),)", 'object_name': 'FacilityCharacter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'sector_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.SectorCategory']"})
        },
        u'dashboard.partner': {
            'Meta': {'ordering': "['name']", 'object_name': 'Partner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'key_activities': ('django.db.models.fields.TextField', [], {}),
            'mission': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        u'dashboard.partnercontribution': {
            'Meta': {'unique_together': "(('country', 'sector_category', 'partner'),)", 'object_name': 'PartnerContribution'},
            'annual_contribution': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '4', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            'financial_contribution': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_kind_contribution': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Partner']"}),
            'sector_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.SectorCategory']"})
        },
        u'dashboard.partnereventcontribution': {
            'Meta': {'unique_together': "(('country', 'sector_category', 'year'),)", 'object_name': 'PartnerEventContribution'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Event']"}),
            'government_staff_contribution': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'own_staff_contribution': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Partner']"}),
            'sector_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.SectorCategory']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Period']"})
        },
        u'dashboard.period': {
            'Meta': {'ordering': "['start_year']", 'object_name': 'Period'},
            'end_year': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_year': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'dashboard.planningperformance': {
            'Meta': {'unique_together': "(('country', 'sector_category', 'year'),)", 'object_name': 'PlanningPerformance'},
            'bottlenecks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            'general_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measures_taken': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'plan_adoption_delay': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'plan_preparation_delay': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sector_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.SectorCategory']"}),
            'success_challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Period']"})
        },
        u'dashboard.priorityarea': {
            'Meta': {'unique_together': "(('country', 'name'),)", 'object_name': 'PriorityArea'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'dashboard.priorityareastatus': {
            'Meta': {'unique_together': "(('priority_area', 'year'),)", 'object_name': 'PriorityAreaStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_households': ('django.db.models.fields.IntegerField', [], {}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'priority_area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PriorityArea']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Period']"})
        },
        u'dashboard.sectorcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'SectorCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        u'dashboard.sectorperformance': {
            'Meta': {'unique_together': "(('country', 'sector_category', 'year'),)", 'object_name': 'SectorPerformance'},
            'bottlenecks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            'coverage_achieved': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'coverage_target': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'fund_availed': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'fund_mobilised': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'fund_needed': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'fund_used': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'general_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measures_taken': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sector_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.SectorCategory']"}),
            'success_challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Period']"})
        },
        u'dashboard.swot': {
            'Meta': {'object_name': 'SWOT'},
            'conclusion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kap_recommendations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mitigation_measures': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'opportunities': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'overall_challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'risks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sector_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.SectorCategory']"}),
            'strengths': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'weaknesses': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'dashboard.technology': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('facility_character', 'name'),)", 'object_name': 'Technology'},
            'facility_character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.FacilityCharacter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'dashboard.tenderprocedureperformance': {
            'Meta': {'unique_together': "(('country', 'tender_procedure_property', 'year'),)", 'object_name': 'TenderProcedurePerformance'},
            'bottlenecks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            'executed': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'general_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measures_taken': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registered': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'success_challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tender_procedure_property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.TenderProcedureProperty']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Period']"})
        },
        u'dashboard.tenderprocedureproperty': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('sector_category', 'name'),)", 'object_name': 'TenderProcedureProperty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'sector_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.SectorCategory']"})
        },
        u'dashboard.usercountry': {
            'Meta': {'ordering': "['country']", 'object_name': 'UserCountry'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['dashboard']