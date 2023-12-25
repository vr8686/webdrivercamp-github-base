from base.environment import report_portal as rp


def scenario_background(context, scenario):
    if 'no_background' in scenario.tags:
        scenario.background = None


def before_all(context):
    rp.before_all(context)


def before_feature(context, feature):
    rp.before_feature(context, feature)


def before_scenario(context, scenario):
    print('SCENARIO\t', scenario.name)
    rp.before_scenario(context, scenario)

    scenario_background(context, scenario)


def before_step(context, step):
    rp.before_step(context, step)


def after_step(context, step):
    print('STEP\t\t', step.name, '\t', step.status)
    if step.status == 'failed':
        chrome.take_screenshot(context)

    rp.after_step(context, step)


def after_scenario(context, scenario):
    print(f'SCENARIO: {scenario.name} - {scenario.status}')
    rp.after_scenario(context, scenario)


def after_feature(context, feature):
    rp.after_feature(context, feature)


def after_all(context):
    rp.after_all(context)
