/**
 * @jest-environment jsdom
 */

//Enable fake timers
jest.useFakeTimers();
jest.spyOn(global, 'setTimeout');

test('remove alerts', () => {
    const removeAlerts = require('../script');
    removeAlerts();
    //Test called 1 times with time 2.5 seconds
    expect(setTimeout).toHaveBeenCalledTimes(1);
    expect(setTimeout).toHaveBeenLastCalledWith(expect.any(Function), 2500);
});
