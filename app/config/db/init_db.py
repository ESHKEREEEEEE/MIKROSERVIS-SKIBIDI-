# import logging
# import datetime
#
# from sqlalchemy.orm import Session
#
# from app import crud
# from app import schemas
# from app.config.db import base  # noqa: F401
# from app.config.default_templates.permissions_settings import (
#     AVAILABLE_ROLES,
#     AVAILABLE_PERMISSIONS,
#     PERMISSION_X_ROLE,
# )
# from app.config.settigns import settings
#
#
# def init_db(db: Session) -> None:
#     # Tables should be created with Alembic migrations
#     # But if you don't want to use migrations, create
#     # the tables un-commenting the next line
#     # Base.metadata.create_all(bind=engine)
#
#     ############
#     # Init Roles
#
#     logging.info("Start Creating Roles")
#     for role_name, meta in AVAILABLE_ROLES.items():
#         role = crud.role.get_by_name(db, name=role_name)
#         if not role:
#             role_in = schemas.RoleCreate(
#                 name=role_name,
#                 description=meta["description"],
#                 access_level=meta["access_level"],
#                 created_at=datetime.datetime.now(),
#                 updated_at=datetime.datetime.now(),
#             )
#             role = crud.role.create(db, obj_in=role_in)
#
#     logging.info("End Creating Roles")
#     # Create permissions
#
#     logging.info("Start Creating Permissions")
#     for permission_name, permission_description in AVAILABLE_PERMISSIONS.items():
#         permission = crud.permission.get_by_name(db, name=permission_name)
#         if not permission:
#             permission_in = schemas.PermissionCreate(
#                 name=permission_name,
#                 description=permission_description,
#                 created_at=datetime.datetime.now(),
#                 updated_at=datetime.datetime.now(),
#             )
#             permission = crud.permission.create(db, obj_in=permission_in)
#
#     logging.info("End Creating Permissions")
#
#     logging.info("Start Adding the Permission to Role")
#     # Add permissions for Roles
#     # 1. Get All roles
#     all_available_roles = crud.role.get_all(db)
#     # 2. Get All Accesses
#     all_available_permissions = crud.permission.get_all(db)
#
#     # 3. Access->Permissions mapping
#     map_permission = {item.name: item.sid for item in all_available_permissions}
#
#     for role in all_available_roles:
#         if role.name not in PERMISSION_X_ROLE.keys():
#             continue
#         current_role_permissions = PERMISSION_X_ROLE[role.name]
#
#         for current_role_permission in current_role_permissions:
#             current_role_permission_sid = map_permission[current_role_permission]
#             permission_x_role = crud.permission_x_role.get_by_permission_and_role(
#                 db, permission_sid=current_role_permission_sid, role_sid=role.sid
#             )
#             if not permission_x_role:
#                 permission_x_role_in = schemas.PermissionXRoleCreate(
#                     permission_sid=current_role_permission_sid, role_sid=role.sid
#                 )
#                 _ = crud.permission_x_role.create(db, obj_in=permission_x_role_in)
#
#         logging.info("End Adding the Permission to Role")
#
#     # Create First SuperUser
#     logging.info("Start Create Superuser")
#
#     superuser = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
#     if not superuser:
#         user_in = schemas.UserCreate(
#             email=settings.FIRST_SUPERUSER,
#             password=settings.FIRST_SUPERUSER_PASSWORD,
#             role="SUPERUSER",
#         )
#         superuser = crud.user.create(db, obj_in=user_in)  # noqa: F841
#
#         superuser_role_sid = crud.role.get_by_name(db, name="SUPERUSER").sid
#
#         superuser_role_in = schemas.UserXRoleCreate(
#             user_sid=superuser.sid, role_sid=superuser_role_sid
#         )
#         crud.user_x_role.create(db, obj_in=superuser_role_in)  # noqa: F841
#         logging.info("End Create Superuser")
