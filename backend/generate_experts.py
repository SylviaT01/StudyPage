# from random import choice, sample
# from flask import current_app
# from app import db, app
# from models import Expert, Service, expert_services, User
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# def generate_experts():
#     logger.info("🌱 Starting Expert Generation...")

#     try:
#         services = Service.query.all()
#         if not services:
#             logger.error("❌ No services found in the database!")
#             return False

#         logger.info(f"Found {len(services)} services")

#         # ✅ Gender-Specific Data
#         male_first_names = [
#             'James', 'Michael', 'William', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Ethan', 'Daniel', 'Matthew',
#             'Jackson', 'Sebastian', 'David', 'Joseph', 'Samuel', 'Carter', 'Owen', 'Wyatt', 'John', 'Jack',
#             'Luke', 'Julian', 'Levi', 'Isaac', 'Anthony', 'Grayson', 'Joshua', 'Christopher', 'Andrew', 'Nathan'
#         ]
#         female_first_names = [
#             'Sarah', 'Emily', 'Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella', 'Mia', 'Charlotte', 'Amelia',
#             'Harper', 'Evelyn', 'Abigail', 'Ella', 'Scarlett', 'Grace', 'Lily', 'Hannah', 'Aria', 'Chloe',
#             'Penelope', 'Riley', 'Zoey', 'Nora', 'Lucy', 'Victoria', 'Madeline', 'Stella', 'Leah', 'Aurora'
#         ]
#         last_names = [
#             'Smith', 'Brown', 'Williams', 'Jones', 'Miller', 'Davis', 'Wilson', 'Anderson', 'Taylor', 'Thomas',
#             'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez',
#             'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'King', 'Wright', 'Scott', 'Green'
#         ]

#         profile_pics_male = [
#             "https://t3.ftcdn.net/jpg/02/43/12/34/360_F_243123463_zTooub557xEWABDLk0jJklDyLSGl2jrr.jpg",
#             "https://t3.ftcdn.net/jpg/03/33/01/30/240_F_333013089_rLm76bpH8O4umraRShSLqLD667bPpvhW.jpg",
#             "https://t3.ftcdn.net/jpg/08/44/38/58/240_F_844385865_TX6AWu9nFXwN9mA2yPvpeTHn8fbndhHq.jpg  ",
#             "https://t3.ftcdn.net/jpg/05/26/60/52/240_F_526605284_O2zMSOvCx4VIGY2nQKlbavo3UW9w0oDF.jpg",
#             "https://t4.ftcdn.net/jpg/10/50/84/95/240_F_1050849528_HMn1btjZvKZHZMc2gfLvSuwn7thAbeno.jpg ",
#             "https://t4.ftcdn.net/jpg/02/54/77/97/240_F_254779767_ROEK4ANl9nl6J1fHhsjnQ8X62Znro9N5.jpg",
#             "https://t4.ftcdn.net/jpg/03/56/33/75/240_F_356337517_lPKBgCGCHYHfmJCV7zlPbvqlf41j66xi.jpg",
#             "https://t4.ftcdn.net/jpg/08/16/92/91/240_F_816929101_gy8vZBUXwLrfYpPazGWPyyi9la4BmRlf.jpg",
#             "https://t4.ftcdn.net/jpg/04/98/99/45/240_F_498994507_BzNm5bADa9GbvxvlgRLFwrc4FetmBmqi.jpg",
#             "https://t3.ftcdn.net/jpg/02/00/90/24/240_F_200902415_G4eZ9Ok3Ypd4SZZKjc8nqJyFVp1eOD6V.jpg",
#             "https://t4.ftcdn.net/jpg/04/22/82/39/240_F_422823992_ZtyrE96o6wGTJcyZolZ6pLRUGHBRCH9c.jpg",
#             "https://t3.ftcdn.net/jpg/02/22/85/16/240_F_222851624_jfoMGbJxwRi5AWGdPgXKSABMnzCQo9RN.jpg",
#             "https://t3.ftcdn.net/jpg/01/70/01/74/240_F_170017413_JHNYFqcpk0aHER9fdnEsETLKafT8rmb0.jpg",
#             "https://t4.ftcdn.net/jpg/04/64/87/43/240_F_464874339_Rc7McGaz327ljzgnWgke4crdDAdI2Yu2.jpg",
#             "https://t4.ftcdn.net/jpg/04/32/89/63/240_F_432896398_99o08tTgBYj8YP2eatvF4zaJu3AdF40E.jpg",
#             "https://t4.ftcdn.net/jpg/02/59/16/27/240_F_259162782_NYDGmbwSM4RQcYC55YAPbVban4G0n5t1.jpg",
#             "https://t3.ftcdn.net/jpg/02/83/12/96/240_F_283129653_iDQrlBEDpYWbKyDIUotS0Dy8ngUwQBaz.jpg",
#             "https://t3.ftcdn.net/jpg/02/07/55/70/240_F_207557081_uh1w4xm9CGqjFLJgrQKYPm9kiASOCPqx.jpg",
#             "https://t3.ftcdn.net/jpg/04/97/66/28/240_F_497662812_7rGW6PMBJR9AbrKcGgN5S1luXYTjH92i.jpg",
#             "https://t4.ftcdn.net/jpg/01/82/22/03/240_F_182220324_QiTjkB3IPwx1zfNltFA4ww3dKQyYvVWB.jpg",
#             "https://t4.ftcdn.net/jpg/03/58/96/39/240_F_358963988_b3FQwLD5wWOmETSvBvLBsBLBtW2z4yUW.jpghttps://t4.ftcdn.net/jpg/03/25/73/59/240_F_325735908_TkxHU7okor9CTWHBhkGfdRumONWfIDEb.jpg",
#             "https://t4.ftcdn.net/jpg/03/86/67/53/240_F_386675348_DkbPRVtBEM55bi2wkGgeEDljzC94rjEu.jpg",
#             "https://t3.ftcdn.net/jpg/03/91/34/72/240_F_391347204_XaDg0S7PtbzJRoeow3yWO1vK4pnqBVQY.jpg",
#             "https://t4.ftcdn.net/jpg/03/64/21/11/240_F_364211147_1qgLVxv1Tcq0Ohz3FawUfrtONzz8nq3e.jpg",
#             "https://t4.ftcdn.net/jpg/06/27/07/63/240_F_627076328_I08lO6C7wYCSjAODeOUyT2ZsyVROe6am.jpg",
#             "https://t4.ftcdn.net/jpg/03/10/07/91/240_F_310079187_l8nBUkpNLpiJ0icGYLAcTbmkxwedmwLO.jpg",
#             "https://t3.ftcdn.net/jpg/07/75/21/26/240_F_775212627_bymcLmHCTPZWAQsuZBMzra3oIEgJLJ36.jpg",
#             "https://t4.ftcdn.net/jpg/03/14/14/45/240_F_314144513_p1hwYePWAvtCR2dD4AiSLJfvLvaxwRub.jpg"
#             "https://t4.ftcdn.net/jpg/02/15/55/93/240_F_215559319_9gwwdzuLgUwt5nW0Tu2baATXQbceyx6y.jpg",
#             "https://t4.ftcdn.net/jpg/01/95/65/17/240_F_195651759_479r5S6Rx77XBSLHJQY2qd2xiwiRGAxB.jpg",
#             "https://t4.ftcdn.net/jpg/02/74/40/77/240_F_274407759_qu3T1jj0UAu9XtSNNB6xHhn7JKKcN2c3.jpg"
#         ]
#         profile_pics_female = [
#             "https://t4.ftcdn.net/jpg/03/83/25/83/240_F_383258331_D8imaEMl8Q3lf7EKU2Pi78Cn0R7KkW9o.jpg",
#             "https://t3.ftcdn.net/jpg/02/43/76/54/240_F_243765470_a0hN5zuTKIonTbRGldi8KajuvhSiWvDx.jpg",
#             "https://t3.ftcdn.net/jpg/02/30/40/74/240_F_230407433_uF2iM6tUs1Sge24999FWdo241t8FMBi7.jpg",
#             "https://t4.ftcdn.net/jpg/03/13/37/31/240_F_313373132_b9Az7XaGLRvSLHXlINXBIGPMIOLok8ZB.jpg",
#             "https://t4.ftcdn.net/jpg/01/51/99/39/240_F_151993994_mmAYzngmSbNRr6Fxma67Od3WHrSkfG5I.jpg",
#             "https://t3.ftcdn.net/jpg/03/36/94/42/240_F_336944276_tpWzmwFi6JfZln5VlfBC1BZu5jgDOAl8.jpg",
#             "https://t4.ftcdn.net/jpg/03/38/90/37/240_F_338903738_RT7vLyCCZeWWvKD42waga3xej2CGFnXW.jpg",
#             "https://t3.ftcdn.net/jpg/03/29/43/72/240_F_329437299_hMz77tiEfQNBbxbX3kRi5HHj4XLlnL4K.jpg",
#             "https://t3.ftcdn.net/jpg/05/43/81/34/240_F_543813442_xjCP4hC52tRTSVp52LSEWr4A12YNyS0l.jpg",
#             "https://t3.ftcdn.net/jpg/03/22/36/32/240_F_322363271_hPT8kGlozwmhfGyA7O08Q7SIvCGUNBhv.jpg",
#             "https://t3.ftcdn.net/jpg/05/22/14/24/240_F_522142457_na0JOOqIXgRMOrgjJItfshoaZlutd3fV.jpg",
#             "https://t4.ftcdn.net/jpg/05/17/69/51/240_F_517695126_xVHlxMfMqZlBw1dtwgtiRKjunSjxX0wj.jpg",
#             "https://t3.ftcdn.net/jpg/02/22/10/62/240_F_222106228_NP5f0gXi3JOCgmaTsEyg7RuyKgwDLGuY.jpg",
#             "https://t4.ftcdn.net/jpg/01/70/01/71/240_F_170017144_y0Y9gnV3q55VNk7dnCRlK4LE1B3e9DFx.jpg",
#             "https://t4.ftcdn.net/jpg/05/35/28/93/240_F_535289317_lrX9mbQwwRd4Bn3kvxL442XjtNJtZxjy.jpg",
#             "https://t3.ftcdn.net/jpg/05/83/41/98/240_F_583419866_97XPxjHDJkQ2RKMmGWdgrbqJhEZeQb55.jpg",
#             "https://t3.ftcdn.net/jpg/02/68/73/32/240_F_268733269_DAOUAU8ioiNKOqRC8PWwji2k5MJQfx1j.jpg",
#             "https://t3.ftcdn.net/jpg/04/14/88/12/240_F_414881258_971wmhPNTLEwKUGXDPJy4Ql7pViomUOl.jpg",
#             "https://t3.ftcdn.net/jpg/03/34/52/14/240_F_334521438_mmtaUtbWMXYCLCtXXNFnivH6wUH60JDc.jpg",
#             "https://t3.ftcdn.net/jpg/07/37/28/54/240_F_737285469_LeX6IZBI4x7wt0VIKkHKVC2o5WfZ4vww.jpg",
#             "https://t4.ftcdn.net/jpg/03/16/72/71/240_F_316727117_LWSUJQxKbgPz4ucNsucp7j3AzGrjJW7U.jpg",
#             "https://t3.ftcdn.net/jpg/04/90/01/32/240_F_490013276_52jMVHNKvG6TJkaUi4Fsh2ICpXEhE3ZG.jpg",
#             "https://t4.ftcdn.net/jpg/03/36/97/95/240_F_336979582_9YQipUAfPEfKF6gZ5EfzT5b8U3vWJsFJ.jpg",
#             "https://t3.ftcdn.net/jpg/03/47/93/50/240_F_347935076_Oqu4VcxwQlh0LT6vrJzxVoxtI71HNmAc.jpg",
#             "https://t3.ftcdn.net/jpg/03/15/07/04/240_F_315070495_eCR5IjbhVfflbx4TPVLrjROgTEfMzjVU.jpg",
#             "https://t3.ftcdn.net/jpg/07/66/62/06/240_F_766620682_pRCdLBW8iq8mS84LWKtpBx4Xu26Cvkl5.jpg",
#             "https://t3.ftcdn.net/jpg/03/55/74/14/240_F_355741445_3NYNN44EbPN7JF7LQQQW7fbhgSTYzNyt.jpg",
#             "https://t3.ftcdn.net/jpg/05/39/16/60/240_F_539166003_yaH6Qx19KpHLbMpegfP7oTX2VFNsCoZk.jpg",
#             "https://t4.ftcdn.net/jpg/05/50/81/29/240_F_550812955_gEsXs9EtB1CUxQD9Bnspgko8AHAwxp8f.jpg",
#             "https://t3.ftcdn.net/jpg/05/13/74/48/240_F_513744811_ERHfVz9cR7pZe8mpvV7JknobjILKBGH7.jpg",
#             "https://t3.ftcdn.net/jpg/05/28/52/94/240_F_528529413_Cjkpm5Ccyr4iwf75vGfOvI4vNJE4rXDu.jpg",
#         ]

#         experts_created = 0
#         for service in services:
#             logger.info(f"🔹 Creating experts for service: {service.title}")
#             used_pics_male, used_pics_female = set(), set()

#             # ✅ Create exactly 3 experts for this service
#             for _ in range(3):
#                 is_male = choice([True, False])
#                 if is_male:
#                     first_name = choice(male_first_names)
#                     available_pics = list(set(profile_pics_male) - used_pics_male)
#                     if not available_pics:
#                         used_pics_male.clear()
#                         available_pics = profile_pics_male
#                     profile_picture = choice(available_pics)
#                     used_pics_male.add(profile_picture)
#                 else:
#                     first_name = choice(female_first_names)
#                     available_pics = list(set(profile_pics_female) - used_pics_female)
#                     if not available_pics:
#                         used_pics_female.clear()
#                         available_pics = profile_pics_female
#                     profile_picture = choice(available_pics)
#                     used_pics_female.add(profile_picture)

#                 last_name = choice(last_names)
#                 full_name = f"{first_name} {last_name}"
#                 new_user = User(
#                     username=full_name,
#                     is_admin=False
#                 )
#                 db.session.add(new_user)
#                 db.session.commit()

#                 # ✅ Create a new expert profile linked to the correct project_type & subject
#                 expert = Expert(
#                     id=new_user.id,
#                     name=full_name,
#                     title=f"{service.title} Specialist",
#                     expertise=f"Expert in {service.title}",
#                     description=f"{full_name} specializes in {service.title}.",
#                     biography="Highly skilled professional with years of experience.",
#                     education="PhD in relevant field",
#                     languages="English, French",
#                     profile_picture=profile_picture,
#                 )

#                 # ✅ Link expert to correct project type and subject
#                 expert.project_types.append(service.project_type)
#                 expert.subjects.append(service.subject)

#                 db.session.add(expert)
#                 db.session.commit()

#                 # ✅ Assign expert to the service
#                 expert.services.append(service)
#                 db.session.commit()
#                 experts_created += 1

#                 logger.info(f"✅ Created expert: {full_name} for '{service.title}'")

#         logger.info(f"✅ Successfully assigned {experts_created} experts!")
#         return True

#     except Exception as e:
#         logger.error(f"❌ Error during expert generation: {str(e)}")
#         db.session.rollback()
#         return False

# if __name__ == "__main__":
#     with app.app_context():
#         success = generate_experts()
#         if not success:
#             logger.error("Expert generation failed!")





from random import choice, sample
from flask import current_app
from app import db, app
from models import Expert, Service, expert_services, User
import logging
from random import uniform, randint
import hashlib

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_experts():
    logger.info("🌱 Starting Expert Generation...")

    try:
        services = Service.query.all()
        if not services:
            logger.error("❌ No services found in the database!")
            return False

        logger.info(f"Found {len(services)} services")

        # ✅ Gender-Specific Data
        male_first_names = [
            'James', 'Michael', 'William', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Ethan', 'Daniel', 'Matthew',
            'Jackson', 'Sebastian', 'David', 'Joseph', 'Samuel', 'Carter', 'Owen', 'Wyatt', 'John', 'Jack',
            'Luke', 'Julian', 'Levi', 'Isaac', 'Anthony', 'Grayson', 'Joshua', 'Christopher', 'Andrew', 'Nathan'
        ]
        female_first_names = [
            'Sarah', 'Emily', 'Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella', 'Mia', 'Charlotte', 'Amelia',
            'Harper', 'Evelyn', 'Abigail', 'Ella', 'Scarlett', 'Grace', 'Lily', 'Hannah', 'Aria', 'Chloe',
            'Penelope', 'Riley', 'Zoey', 'Nora', 'Lucy', 'Victoria', 'Madeline', 'Stella', 'Leah', 'Aurora'
        ]
        last_names = [
            'Smith', 'Brown', 'Williams', 'Jones', 'Miller', 'Davis', 'Wilson', 'Anderson', 'Taylor', 'Thomas',
            'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez',
            'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'King', 'Wright', 'Scott', 'Green'
        ]

        profile_pics_male = [
            "https://t3.ftcdn.net/jpg/02/43/12/34/360_F_243123463_zTooub557xEWABDLk0jJklDyLSGl2jrr.jpg",
            "https://t3.ftcdn.net/jpg/03/33/01/30/240_F_333013089_rLm76bpH8O4umraRShSLqLD667bPpvhW.jpg",
            "https://t3.ftcdn.net/jpg/08/44/38/58/240_F_844385865_TX6AWu9nFXwN9mA2yPvpeTHn8fbndhHq.jpg  ",
            "https://t3.ftcdn.net/jpg/05/26/60/52/240_F_526605284_O2zMSOvCx4VIGY2nQKlbavo3UW9w0oDF.jpg",
            "https://t4.ftcdn.net/jpg/10/50/84/95/240_F_1050849528_HMn1btjZvKZHZMc2gfLvSuwn7thAbeno.jpg ",
            "https://t4.ftcdn.net/jpg/02/54/77/97/240_F_254779767_ROEK4ANl9nl6J1fHhsjnQ8X62Znro9N5.jpg",
            "https://t4.ftcdn.net/jpg/03/56/33/75/240_F_356337517_lPKBgCGCHYHfmJCV7zlPbvqlf41j66xi.jpg",
            "https://t4.ftcdn.net/jpg/08/16/92/91/240_F_816929101_gy8vZBUXwLrfYpPazGWPyyi9la4BmRlf.jpg",
            "https://t4.ftcdn.net/jpg/04/98/99/45/240_F_498994507_BzNm5bADa9GbvxvlgRLFwrc4FetmBmqi.jpg",
            "https://t3.ftcdn.net/jpg/02/00/90/24/240_F_200902415_G4eZ9Ok3Ypd4SZZKjc8nqJyFVp1eOD6V.jpg",
            "https://t4.ftcdn.net/jpg/04/22/82/39/240_F_422823992_ZtyrE96o6wGTJcyZolZ6pLRUGHBRCH9c.jpg",
            "https://t3.ftcdn.net/jpg/02/22/85/16/240_F_222851624_jfoMGbJxwRi5AWGdPgXKSABMnzCQo9RN.jpg",
            "https://t3.ftcdn.net/jpg/01/70/01/74/240_F_170017413_JHNYFqcpk0aHER9fdnEsETLKafT8rmb0.jpg",
            "https://t4.ftcdn.net/jpg/04/64/87/43/240_F_464874339_Rc7McGaz327ljzgnWgke4crdDAdI2Yu2.jpg",
            "https://t4.ftcdn.net/jpg/04/32/89/63/240_F_432896398_99o08tTgBYj8YP2eatvF4zaJu3AdF40E.jpg",
            "https://t4.ftcdn.net/jpg/02/59/16/27/240_F_259162782_NYDGmbwSM4RQcYC55YAPbVban4G0n5t1.jpg",
            "https://t3.ftcdn.net/jpg/02/83/12/96/240_F_283129653_iDQrlBEDpYWbKyDIUotS0Dy8ngUwQBaz.jpg",
            "https://t3.ftcdn.net/jpg/02/07/55/70/240_F_207557081_uh1w4xm9CGqjFLJgrQKYPm9kiASOCPqx.jpg",
            "https://t3.ftcdn.net/jpg/04/97/66/28/240_F_497662812_7rGW6PMBJR9AbrKcGgN5S1luXYTjH92i.jpg",
            "https://t4.ftcdn.net/jpg/01/82/22/03/240_F_182220324_QiTjkB3IPwx1zfNltFA4ww3dKQyYvVWB.jpg",
            "https://t4.ftcdn.net/jpg/03/58/96/39/240_F_358963988_b3FQwLD5wWOmETSvBvLBsBLBtW2z4yUW.jpghttps://t4.ftcdn.net/jpg/03/25/73/59/240_F_325735908_TkxHU7okor9CTWHBhkGfdRumONWfIDEb.jpg",
            "https://t4.ftcdn.net/jpg/03/86/67/53/240_F_386675348_DkbPRVtBEM55bi2wkGgeEDljzC94rjEu.jpg",
            "https://t3.ftcdn.net/jpg/03/91/34/72/240_F_391347204_XaDg0S7PtbzJRoeow3yWO1vK4pnqBVQY.jpg",
            "https://t4.ftcdn.net/jpg/03/64/21/11/240_F_364211147_1qgLVxv1Tcq0Ohz3FawUfrtONzz8nq3e.jpg",
            "https://t4.ftcdn.net/jpg/06/27/07/63/240_F_627076328_I08lO6C7wYCSjAODeOUyT2ZsyVROe6am.jpg",
            "https://t4.ftcdn.net/jpg/03/10/07/91/240_F_310079187_l8nBUkpNLpiJ0icGYLAcTbmkxwedmwLO.jpg",
            "https://t3.ftcdn.net/jpg/07/75/21/26/240_F_775212627_bymcLmHCTPZWAQsuZBMzra3oIEgJLJ36.jpg",
            "https://t4.ftcdn.net/jpg/03/14/14/45/240_F_314144513_p1hwYePWAvtCR2dD4AiSLJfvLvaxwRub.jpg"
            "https://t4.ftcdn.net/jpg/02/15/55/93/240_F_215559319_9gwwdzuLgUwt5nW0Tu2baATXQbceyx6y.jpg",
            "https://t4.ftcdn.net/jpg/01/95/65/17/240_F_195651759_479r5S6Rx77XBSLHJQY2qd2xiwiRGAxB.jpg",
            "https://t4.ftcdn.net/jpg/02/74/40/77/240_F_274407759_qu3T1jj0UAu9XtSNNB6xHhn7JKKcN2c3.jpg"
        ]
        profile_pics_female = [
            "https://t4.ftcdn.net/jpg/03/83/25/83/240_F_383258331_D8imaEMl8Q3lf7EKU2Pi78Cn0R7KkW9o.jpg",
            "https://t3.ftcdn.net/jpg/02/43/76/54/240_F_243765470_a0hN5zuTKIonTbRGldi8KajuvhSiWvDx.jpg",
            "https://t3.ftcdn.net/jpg/02/30/40/74/240_F_230407433_uF2iM6tUs1Sge24999FWdo241t8FMBi7.jpg",
            "https://t4.ftcdn.net/jpg/03/13/37/31/240_F_313373132_b9Az7XaGLRvSLHXlINXBIGPMIOLok8ZB.jpg",
            "https://t4.ftcdn.net/jpg/01/51/99/39/240_F_151993994_mmAYzngmSbNRr6Fxma67Od3WHrSkfG5I.jpg",
            "https://t3.ftcdn.net/jpg/03/36/94/42/240_F_336944276_tpWzmwFi6JfZln5VlfBC1BZu5jgDOAl8.jpg",
            "https://t4.ftcdn.net/jpg/03/38/90/37/240_F_338903738_RT7vLyCCZeWWvKD42waga3xej2CGFnXW.jpg",
            "https://t3.ftcdn.net/jpg/03/29/43/72/240_F_329437299_hMz77tiEfQNBbxbX3kRi5HHj4XLlnL4K.jpg",
            "https://t3.ftcdn.net/jpg/05/43/81/34/240_F_543813442_xjCP4hC52tRTSVp52LSEWr4A12YNyS0l.jpg",
            "https://t3.ftcdn.net/jpg/03/22/36/32/240_F_322363271_hPT8kGlozwmhfGyA7O08Q7SIvCGUNBhv.jpg",
            "https://t3.ftcdn.net/jpg/05/22/14/24/240_F_522142457_na0JOOqIXgRMOrgjJItfshoaZlutd3fV.jpg",
            "https://t4.ftcdn.net/jpg/05/17/69/51/240_F_517695126_xVHlxMfMqZlBw1dtwgtiRKjunSjxX0wj.jpg",
            "https://t3.ftcdn.net/jpg/02/22/10/62/240_F_222106228_NP5f0gXi3JOCgmaTsEyg7RuyKgwDLGuY.jpg",
            "https://t4.ftcdn.net/jpg/01/70/01/71/240_F_170017144_y0Y9gnV3q55VNk7dnCRlK4LE1B3e9DFx.jpg",
            "https://t4.ftcdn.net/jpg/05/35/28/93/240_F_535289317_lrX9mbQwwRd4Bn3kvxL442XjtNJtZxjy.jpg",
            "https://t3.ftcdn.net/jpg/05/83/41/98/240_F_583419866_97XPxjHDJkQ2RKMmGWdgrbqJhEZeQb55.jpg",
            "https://t3.ftcdn.net/jpg/02/68/73/32/240_F_268733269_DAOUAU8ioiNKOqRC8PWwji2k5MJQfx1j.jpg",
            "https://t3.ftcdn.net/jpg/04/14/88/12/240_F_414881258_971wmhPNTLEwKUGXDPJy4Ql7pViomUOl.jpg",
            "https://t3.ftcdn.net/jpg/03/34/52/14/240_F_334521438_mmtaUtbWMXYCLCtXXNFnivH6wUH60JDc.jpg",
            "https://t3.ftcdn.net/jpg/07/37/28/54/240_F_737285469_LeX6IZBI4x7wt0VIKkHKVC2o5WfZ4vww.jpg",
            "https://t4.ftcdn.net/jpg/03/16/72/71/240_F_316727117_LWSUJQxKbgPz4ucNsucp7j3AzGrjJW7U.jpg",
            "https://t3.ftcdn.net/jpg/04/90/01/32/240_F_490013276_52jMVHNKvG6TJkaUi4Fsh2ICpXEhE3ZG.jpg",
            "https://t4.ftcdn.net/jpg/03/36/97/95/240_F_336979582_9YQipUAfPEfKF6gZ5EfzT5b8U3vWJsFJ.jpg",
            "https://t3.ftcdn.net/jpg/03/47/93/50/240_F_347935076_Oqu4VcxwQlh0LT6vrJzxVoxtI71HNmAc.jpg",
            "https://t3.ftcdn.net/jpg/03/15/07/04/240_F_315070495_eCR5IjbhVfflbx4TPVLrjROgTEfMzjVU.jpg",
            "https://t3.ftcdn.net/jpg/07/66/62/06/240_F_766620682_pRCdLBW8iq8mS84LWKtpBx4Xu26Cvkl5.jpg",
            "https://t3.ftcdn.net/jpg/03/55/74/14/240_F_355741445_3NYNN44EbPN7JF7LQQQW7fbhgSTYzNyt.jpg",
            "https://t3.ftcdn.net/jpg/05/39/16/60/240_F_539166003_yaH6Qx19KpHLbMpegfP7oTX2VFNsCoZk.jpg",
            "https://t4.ftcdn.net/jpg/05/50/81/29/240_F_550812955_gEsXs9EtB1CUxQD9Bnspgko8AHAwxp8f.jpg",
            "https://t3.ftcdn.net/jpg/05/13/74/48/240_F_513744811_ERHfVz9cR7pZe8mpvV7JknobjILKBGH7.jpg",
            "https://t3.ftcdn.net/jpg/05/28/52/94/240_F_528529413_Cjkpm5Ccyr4iwf75vGfOvI4vNJE4rXDu.jpg",
        ]

        professional_titles = {
            "Dissertation": ["Dissertation Specialist", "Research Methodologist", "Doctoral Advisor"],
            "Thesis": ["Thesis Consultant", "Research Scholar", "Academic Advisor"],
            "Research Paper": ["Research Analyst", "Academic Writer", "Research Specialist"],
            "Business Plan": ["Business Strategist", "Business Development Consultant", "Strategic Planning Expert"],
            "Case Study": ["Case Study Specialist", "Analysis Expert", "Applied Research Consultant"],
            "Technical Report": ["Technical Documentation Specialist", "Technical Writer", "Engineering Documentation Expert"],
            "Data Analysis": ["Data Scientist", "Statistical Analyst", "Quantitative Research Specialist"],
            "Lab Report": ["Laboratory Specialist", "Scientific Writer", "Experimental Research Analyst"],
            "Code": ["Software Developer", "Programming Expert", "Code Implementation Specialist"],
            "Math Solving": ["Mathematics Expert", "Quantitative Problem Solver", "Mathematical Modeling Specialist"],
            "Literature Review": ["Literature Analysis Expert", "Research Literature Specialist", "Bibliographic Consultant"],
            "Essay": ["Essay Writing Expert", "Composition Specialist", "Academic Writing Consultant"],
            "Article": ["Article Writer", "Content Specialist", "Publication Expert"],
            "Creative Writing": ["Creative Content Developer", "Narrative Specialist", "Creative Writing Consultant"],
            "Content Writing": ["Content Strategist", "Content Development Expert", "Digital Content Specialist"],
            "Editing": ["Professional Editor", "Content Refinement Specialist", "Editorial Consultant"],
            "Outline": ["Structure Development Specialist", "Outline Design Expert", "Framework Consultant"],
            "Presentation": ["Presentation Designer", "Visual Communication Expert", "Slide Deck Specialist"],
            "Proposal": ["Proposal Development Expert", "Grant Writing Specialist", "Project Proposal Consultant"],
            "Personal Statement": ["Personal Narrative Specialist", "Admissions Document Expert", "Application Document Consultant"],
            "Application Essay": ["Admissions Consultant", "Application Strategy Expert", "Personal Branding Specialist"],
            "Annotated Bibliography": ["Bibliographic Research Specialist", "Citation Analysis Expert", "Research Documentation Consultant"],
            "Coursework": ["Academic Coursework Specialist", "Curriculum Expert", "Academic Assignment Consultant"],
            "Excel Assignment": ["Excel Modeling Expert", "Data Visualization Specialist", "Spreadsheet Analysis Consultant"]
        }
        
        # ✅ Subject-specific education and expertise
        education_by_subject = {
            "Engineering": ["Ph.D. in Engineering", "Master of Engineering", "B.Sc. in Engineering with Honors"],
            "Computer Science": ["Ph.D. in Computer Science", "M.Sc. in Computer Science", "B.Sc. in Computer Science with Honors"],
            "Mathematics": ["Ph.D. in Mathematics", "M.Sc. in Applied Mathematics", "B.Sc. in Mathematics with Honors"],
            "Nursing": ["Doctor of Nursing Practice (DNP)", "Master of Science in Nursing (MSN)", "B.Sc. in Nursing with Clinical Distinction"],
            "Biology": ["Ph.D. in Biological Sciences", "M.Sc. in Biology", "B.Sc. in Biology with Research Honors"],
            "Physics": ["Ph.D. in Physics", "M.Sc. in Applied Physics", "B.Sc. in Physics with Honors"],
            "Economics": ["Ph.D. in Economics", "Master of Economics", "B.A. in Economics with Honors"],
            "Business": ["MBA with Specialization", "Master of Business Administration", "B.B.A. with Honors"],
            "Law": ["Juris Doctor (J.D.)", "Master of Laws (LL.M.)", "Bachelor of Laws (LL.B.)"],
            "Psychology": ["Ph.D. in Psychology", "M.Sc. in Clinical Psychology", "B.A. in Psychology with Honors"],
            "Finance": ["Ph.D. in Finance", "Master of Finance", "B.Sc. in Finance with Honors"],
            "Marketing": ["Ph.D. in Marketing", "Master of Marketing", "B.B.A. in Marketing with Honors"],
            "Operations Management": ["Ph.D. in Operations Management", "M.Sc. in Operations Research", "B.B.A. in Operations Management"],
            "Criminal Justice": ["Ph.D. in Criminal Justice", "Master of Criminal Justice", "B.A. in Criminal Justice with Honors"],
            "Statistics": ["Ph.D. in Statistics", "M.Sc. in Applied Statistics", "B.Sc. in Statistics with Honors"],
            "Operations Research": ["Ph.D. in Operations Research", "M.Sc. in Operations Research", "B.Sc. in Mathematics with OR Specialization"],
            "Data Analysis": ["Ph.D. in Data Science", "M.Sc. in Analytics", "B.Sc. in Data Science with Honors"],
            "Chemistry": ["Ph.D. in Chemistry", "M.Sc. in Chemistry", "B.Sc. in Chemistry with Honors"],
            "Environmental Science": ["Ph.D. in Environmental Science", "M.Sc. in Environmental Studies", "B.Sc. in Environmental Science with Honors"],
            "Information Technology": ["Ph.D. in Information Technology", "M.Sc. in IT", "B.Sc. in Information Technology with Honors"],
            "Web Development": ["Master of Web Development", "B.Sc. in Computer Science with Web Development Focus", "Full Stack Development Certification"],
            "Algebra": ["Ph.D. in Mathematics (Algebraic Specialization)", "M.Sc. in Pure Mathematics", "B.Sc. in Mathematics with Honors"],
            "English": ["Ph.D. in English Literature", "M.A. in English", "B.A. in English with Honors"],
            "History": ["Ph.D. in History", "M.A. in Historical Studies", "B.A. in History with Honors"],
            "Literature": ["Ph.D. in Comparative Literature", "M.A. in Literature", "B.A. in Literature with Honors"],
            "Sociology": ["Ph.D. in Sociology", "M.A. in Sociological Studies", "B.A. in Sociology with Honors"],
            "Journalism": ["Ph.D. in Journalism", "Master of Journalism", "B.A. in Journalism with Honors"],
            "Communications": ["Ph.D. in Communications", "M.A. in Communication Studies", "B.A. in Communications with Honors"],
            "Public Relations": ["Ph.D. in Public Relations", "M.A. in PR & Strategic Communications", "B.A. in Public Relations with Honors"],
            "Creative Writing": ["M.F.A. in Creative Writing", "M.A. in Creative Writing", "B.A. in English with Creative Writing Focus"],
            "Digital Media": ["Ph.D. in Digital Media", "M.A. in Digital Media Studies", "B.A. in Digital Media with Honors"],
            "Research Methods": ["Ph.D. in Research Methodology", "M.Sc. in Research Methods", "B.Sc. with Research Methods Focus"],
            "Education": ["Ed.D. in Education", "M.Ed. in Educational Leadership", "B.Ed. with Honors"]
        }
        
        # Default for subjects not in the list
        default_education = ["Ph.D. in the Field", "Master's Degree", "Bachelor's Degree with Honors"]
        
        # ✅ Expertise templates by project type
        expertise_templates = {
            "Dissertation": [
                "{years} years of experience guiding doctoral candidates through dissertation research and writing",
                "Specialist in {subject} dissertation methodology and research design with {years} years of experience",
                "Expert dissertation advisor with {years} years of experience in {subject} research methods"
            ],
            "Research Paper": [
                "Published researcher with {years} years of experience in {subject} studies",
                "Research specialist with {papers} published papers in peer-reviewed {subject} journals",
                "{subject} research expert with {years} years of academic and industry experience"
            ],
            "Essay": [
                "Professional {subject} essay writer with {years} years of experience in academic writing",
                "Experienced {subject} content specialist with expertise in argumentative and analytical essays",
                "Academic writing expert specializing in {subject} essays and critical analysis"
            ],
            "Code": [
                "Software developer with {years} years of professional coding experience in {subject}",
                "{subject} programmer with expertise in multiple programming languages and frameworks",
                "Technical developer specializing in {subject} with {years} years of industry experience"
            ]
        }
        # Default expertise template for project types not specifically listed
        default_expertise_templates = [
            "Specialist in {subject} with {years} years of professional experience",
            "Experienced {subject} professional with expertise in {project_type}",
            "{subject} expert with {years} years of academic and industry experience"
        ]
        
        # ✅ Professional biography templates
        biography_templates = [
            "{name} is a seasoned professional with {years} years of experience in {subject}. With a {education} and professional background in {industry}, {pronoun} has successfully completed over {projects} projects in {project_type}. {pronoun_cap} specializes in {specialty} and has a proven track record of delivering high-quality work that exceeds client expectations.",
            
            "With {years} years of dedicated experience in {subject}, {name} brings exceptional expertise to every {project_type} project. Holding a {education}, {pronoun} has developed specialized knowledge in {specialty}. {pronoun_cap} has worked with clients ranging from students to industry professionals, completing more than {projects} successful projects.",
            
            "{name} is a {subject} expert with a {education} and {years} years of practical experience. {pronoun_cap} has extensive experience in {project_type} development, having completed {projects}+ projects with outstanding client satisfaction. {pronoun_cap} is known for {specialty} and delivering results that consistently exceed expectations.",
            
            "As an experienced {subject} specialist with a {education}, {name} has dedicated {years} years to mastering the complexities of {project_type}. {pronoun_cap} has successfully guided {projects}+ clients through their projects, specializing in {specialty}. {pronoun_cap} brings a methodical approach and attention to detail to every project."
        ]
        
        # ✅ Language combinations
        language_options = [
            "English, Spanish",
            "English, French, German",
            "English, Mandarin",
            "English, Arabic",
            "English, Russian",
            "English, Portuguese",
            "English, Japanese",
            "English, Hindi",
            "English, Italian",
            "English only (native)"
        ]
        
        # Industries by subject
        industries = {
            "Engineering": ["aerospace", "automotive", "construction", "energy"],
            "Computer Science": ["software development", "IT consulting", "cybersecurity", "tech startups"],
            "Business": ["management consulting", "corporate strategy", "entrepreneurship"],
            "Law": ["legal practice", "corporate law", "intellectual property"],
            "Psychology": ["clinical practice", "research psychology", "organizational psychology"],
            "Economics": ["economic consulting", "financial analysis", "policy research"]
        }
        # Default industries for subjects not in the list
        default_industries = ["academic research", "professional consulting", "education", "private practice"]

        # ✅ Specialties by project type and subject
        specialties = {
            "Dissertation": {
                "Engineering": ["structural analysis methodologies", "engineering design optimization", "systems engineering approaches"],
                "Psychology": ["qualitative research methods", "experimental psychology design", "longitudinal study methodologies"]
            },
            "Research Paper": {
                "Economics": ["econometric analysis", "economic policy evaluation", "market structure analysis"],
                "Business": ["strategic management research", "organizational behavior studies", "market research methodologies"]
            }
        }
        # Default specialties
        default_specialties = ["comprehensive research methodologies", "detailed analytical approaches", "clear and concise communication"]

        experts_created = 0
        for service in services:
            # Extract project type and subject from service title
            service_parts = service.title.split(" - ")
            if len(service_parts) >= 2:
                project_type = service_parts[0]
                subject = service_parts[1]
            else:
                # Fallback if title format is different
                project_type = service.project_type.name if hasattr(service, 'project_type') and hasattr(service.project_type, 'name') else "General"
                subject = service.subject.name if hasattr(service, 'subject') and hasattr(service.subject, 'name') else "General"
                
            logger.info(f"🔹 Creating experts for service: {service.title}")
            used_pics_male, used_pics_female = set(), set()

            # ✅ Create exactly 3 experts for this service
            for i in range(3):
                is_male = choice([True, False])
                
                # Generate professional name
                if is_male:
                    first_name = choice(male_first_names)
                    pronoun = "he"
                    pronoun_cap = "He"
                    available_pics = list(set(profile_pics_male) - used_pics_male)
                    if not available_pics:
                        used_pics_male.clear()
                        available_pics = profile_pics_male
                    profile_picture = choice(available_pics)
                    used_pics_male.add(profile_picture)
                else:
                    first_name = choice(female_first_names)
                    pronoun = "she"
                    pronoun_cap = "She"
                    available_pics = list(set(profile_pics_female) - used_pics_female)
                    if not available_pics:
                        used_pics_female.clear()
                        available_pics = profile_pics_female
                    profile_picture = choice(available_pics)
                    used_pics_female.add(profile_picture)

                last_name = choice(last_names)
                full_name = f"{first_name} {last_name}"
                
                # ✅ Generate a professional username
                username_options = [
                    f"{first_name.lower()}.{last_name.lower()}",
                    f"{first_name.lower()}{last_name.lower()}",
                    f"{first_name[0].lower()}{last_name.lower()}",
                    f"{last_name.lower()}.{first_name.lower()}",
                    f"prof.{last_name.lower()}"
                ]
                
                # Add a number to username to ensure uniqueness if needed
                username_base = choice(username_options)
                username = username_base
                
                # Check if username exists and add a number if it does
                existing_user = User.query.filter_by(username=username).first()
                if existing_user:
                    # Hash the name to get a consistent but unique number
                    name_hash = int(hashlib.md5(full_name.encode()).hexdigest(), 16) % 1000
                    username = f"{username_base}{name_hash}"
                
                # Create the user
                new_user = User(
                    username=username,
                    is_admin=False
                )
                db.session.add(new_user)
                db.session.commit()
                
                # ✅ Generate professional title
                if project_type in professional_titles:
                    title = f"{choice(professional_titles[project_type])} in {subject}"
                else:
                    title = f"{subject} Specialist"
                
                # ✅ Generate education background
                if subject in education_by_subject:
                    education = choice(education_by_subject[subject])
                else:
                    education = choice(default_education)
                
                # ✅ Generate experience years and projects count
                years_experience = randint(5, 20)
                projects_completed = randint(50, 500)
                papers_published = randint(5, 25)
                
                # ✅ Generate expertise description
                if project_type in expertise_templates:
                    expertise_template = choice(expertise_templates[project_type])
                else:
                    expertise_template = choice(default_expertise_templates)
                
                expertise = expertise_template.format(
                    subject=subject,
                    years=years_experience,
                    papers=papers_published,
                    project_type=project_type
                )
                
                # ✅ Generate industry
                if subject in industries:
                    industry = choice(industries[subject])
                else:
                    industry = choice(default_industries)
                
                # ✅ Generate specialty
                if project_type in specialties and subject in specialties[project_type]:
                    specialty = choice(specialties[project_type][subject])
                else:
                    specialty = choice(default_specialties)
                
                # ✅ Generate biography
                biography_template = choice(biography_templates)
                biography = biography_template.format(
                    name=full_name,
                    years=years_experience,
                    subject=subject,
                    education=education,
                    industry=industry,
                    pronoun=pronoun,
                    pronoun_cap=pronoun_cap,
                    projects=projects_completed,
                    project_type=project_type,
                    specialty=specialty
                )
                
                # ✅ Generate languages
                languages = choice(language_options)
                
                # ✅ Generate random ratings and success rate
                rating_avg = round(uniform(4.5, 5.0), 1)
                total_reviews = randint(10, 100)
                success_rate = round(uniform(92.0, 99.5), 1)
                
                # ✅ Generate description
                description = f"Experienced {subject} specialist with a focus on {project_type}. {pronoun_cap} has helped clients achieve exceptional results through meticulous attention to detail and expert knowledge."
                
                # ✅ Create the expert profile
                expert = Expert(
                    id=new_user.id,
                    name=full_name,
                    title=title,
                    expertise=expertise,
                    description=description,
                    biography=biography,
                    education=education,
                    languages=languages,
                    profile_picture=profile_picture,
                    rating_avg=rating_avg,
                    total_reviews=total_reviews,
                    success_rate=success_rate,
                    is_ai_free=True  # Assuming all experts are AI-free by default
                )

                # ✅ Link expert to correct project type and subject
                expert.project_types.append(service.project_type)
                expert.subjects.append(service.subject)

                db.session.add(expert)
                db.session.commit()

                # ✅ Assign expert to the service
                expert.services.append(service)
                db.session.commit()
                experts_created += 1

                logger.info(f"✅ Created expert: {full_name} (username: {username}) for '{service.title}'")

        logger.info(f"✅ Successfully assigned {experts_created} experts!")
        return True

    except Exception as e:
        logger.error(f"❌ Error during expert generation: {str(e)}")
        db.session.rollback()
        return False

if __name__ == "__main__":
    with app.app_context():
        success = generate_experts()
        if not success:
            logger.error("Expert generation failed!")

