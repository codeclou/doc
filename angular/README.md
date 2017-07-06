# Angular Styleguide

## Preconditions

 * We use IntelliJ
 * We use TypeScript
 * We use Tslint
 * We use Angular CLI and the tslint config from there

## General Rules

 * Single Quotes
 * Spacing between curly braces
 * dangling comma (for better git diffs)


:red_circle: BAD

```typescript
import {Foo} from "foo";
```

:white_check_mark: GOOD

```typescript
import { Foo } from 'foo';
```

:red_circle: BAD

```typescript
const foo = {
  bar: 'x',
  foo: 'y'
};
```

:white_check_mark: GOOD (dangling comma)

```typescript
const foo = {
  bar: 'x',
  foo: 'y',
};
```


## IntelliJ



