import { mount } from 'enzyme';
import 'jest-enzyme';

import App from "../App";

describe("<App />", () => {
    it('renders', () => {
        const wrapper = mount(<App />)
        expect(wrapper).toContainMatchingElements(1, "CurrencyTable")
    });
})
