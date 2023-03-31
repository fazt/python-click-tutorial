#!/usr/bin/env python
import json_manager
import click


@click.group()
def cli():
    pass

# crear


@cli.command()
@click.option('--name', required=True, help="user's name")
@click.option('--lastname', required=True, help="user's lastname")
@click.pass_context
def new(ctx, name, lastname):
    """Crear un nuevo registro."""
    if not name or not lastname:
        ctx.fail('the name and lastname are required')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        nuevo_registro = {'id': new_id, 'name': name, 'lastname': lastname}
        data.append(nuevo_registro)
        json_manager.write_json(data)
        print(f"new user created with id {new_id}")


@cli.command()
def users():
    data = json_manager.read_json()
    for user in data:
        print(
            f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print('user does not exist')
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument('id', type=int)
@click.option('--name', default=None)
@click.option('--lastname', default=None)
def update(id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break
    json_manager.write_json(data)


@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print('user not found')
    else:
        data.remove(user)
        json_manager.write_json(data)


if __name__ == '__main__':
    cli()
