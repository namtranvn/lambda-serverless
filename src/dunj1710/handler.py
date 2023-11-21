import logging
import traceback

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    try:
        logger.info(f"EVENT: {event}")
        logger.info(f"CONTEXT: {context}")
        # TODO implement your function
        
        


        return {"status": "SUCCESS"}
    except Exception as ex:
        logger.error(f'FATAL ERROR: {ex} %s')
        logger.error('TRACEBACK:')
        logger.error(traceback.format_exc())

        return {"status": "FAIL", "error": f"{ex}"}
